import discord
from discord import app_commands
from discord.ext import commands
from mcrcon import MCRcon
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

logging.info("Starting bot...")

# Set up the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Minecraft RCON credentials (replace these)
RCON_HOST = os.getenv('HOST')
RCON_PORT = int(os.getenv('PORT'))
RCON_PASSWORD = os.getenv('PASSWORD')

logging.info(f'RCON credentials: HOST={RCON_HOST}, PORT={RCON_PORT}, PASSWORD={"[REDACTED]" if RCON_PASSWORD else None}')

# Command to whitelist a player
@bot.tree.command(name='whitelist', description='Whitelist a player on the Minecraft server')
async def whitelist(interaction: discord.Interaction, username: str):
    logging.info(f'Attempting to whitelist {username} by {interaction.user}')
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, RCON_PORT) as mcr:
            response = mcr.command(f'whitelist add {username}')
            logging.info(f'Whitelist response: {response}')
            await interaction.response.send_message(f'Player {username} has been whitelisted.')
    except Exception as e:
        logging.error(f'Failed to whitelist {username}: {e}')
        await interaction.response.send_message(f'Failed to whitelist {username}. Error: {e}')

# Command to list server info
@bot.tree.command(name='info', description='List server info')
async def info(interaction: discord.Interaction):
    logging.info(f'Info command used by {interaction.user}')
    await interaction.response.send_message(f'The server id is mc.carsonmayn.com \n Get the mods at mod.carsonmayn.com .\n Thank you for using the bot.')

# Admin-only RCON command
@bot.tree.command(name='drcon', description='Admin only')
async def drcon(interaction: discord.Interaction, rcon: str):
    logging.info(f'RCON command used by {interaction.user}: {rcon}')
    if str(interaction.user) == "ocueye":
        try:
            with MCRcon(RCON_HOST, RCON_PASSWORD, RCON_PORT) as mcr:
                response = mcr.command(rcon)
                logging.info(f'RCON response: {response}')
                await interaction.response.send_message(response)
        except Exception as e:
            logging.error(f'Error running RCON command {rcon}: {e}')
            await interaction.response.send_message(f'Error running {rcon}.\nError: {e}')
    else:
        logging.warning(f'Unauthorized user {interaction.user} attempted to run RCON command {rcon}')
        await interaction.response.send_message(f'Error: You do not have the privilege to use this command')

@bot.event
async def on_ready():
    await bot.tree.sync()
    logging.info(f'Logged in as {bot.user}!')

# Run the bot
bot.run(os.getenv('KEY'))
