from python:3.11.1-buster

# Define your working directory
WORKDIR /

# Install runpod
RUN pip install runpod

# Add my handler
ADD handler.py .

# Call your handler when the container starts
CMD [ "python", "-u", "/handler.py" ]
