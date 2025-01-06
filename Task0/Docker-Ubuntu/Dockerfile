# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# List the contents of the /app directory for debugging
RUN ls -la /app

# Run main.py when the container launches
CMD ["python3", "main.py"]


#build Docker image
# docker build -t my-ubuntu-app .
#run Docker container
# docker run my-ubuntu-app


# docker build -t my-ubuntu-app .
# docker run -it --rm my-ubuntu-app