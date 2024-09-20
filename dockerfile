# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set Python to not buffer stdout/stderr (important for Docker logging)
ENV PYTHONUNBUFFERED=1

# Update package lists and install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy your script and requirements.txt into the container
COPY start.py .
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Set environment variables
ENV KEY=KEY
ENV HOST=HOST
ENV PORT=PORT
ENV PASSWORD=PASSWORD

# Command to run your Python script
CMD ["python3", "bot.py"]
