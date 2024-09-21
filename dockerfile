# Start with your base image
FROM  python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install discord pycord mcrcon
# Copy the rest of your application code into the container at /app
COPY . .


# Run app.py when the container launches
CMD ["python", "bot.py"]
