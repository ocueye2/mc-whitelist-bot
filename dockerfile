# Dockerfile
FROM python:3.10-slim


# Copy your script
COPY start.py .

# Install dependencies if necessary
RUN pip install -r requirements.txt

# Set the environment variable
ENV KEY=KEY
ENV HOST=HOST
ENV PORT=PORT
ENV PASSWORD=PASSWORD
# Command to run your script
CMD ["python", "bot.py"]
