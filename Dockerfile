# Marakulin Andrey @annndruha
# 2021
ARG PROJECT_NAME=vk_api_docker_shell

# Base image
FROM python:3.7.9-stretch

# Create directoris inside container
ADD ./ /$PROJECT_NAME
WORKDIR /$PROJECT_NAME

# Install libs from requirements
RUN pip install --upgrade pip==20.3.3
RUN pip install --no-cache-dir -r requirements.txt

# Specify the port number the container should expose 
EXPOSE 4242

# Run the file
CMD ["python", "-u", "./main.py"]
