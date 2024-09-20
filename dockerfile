# Dockerfile
FROM ubuntu:22.04



# Copy your script
COPY start.py .

CMD sudo apt install python3 python3-pip

# Install dependencies if necessary
RUN pip install -r requirements.txt

# Set the environment variable
ENV KEY=KEY
ENV HOST=HOST
ENV PORT=PORT
ENV PASSWORD=PASSWORD
# Command to run your script
CMD ["python", "bot.py"]
