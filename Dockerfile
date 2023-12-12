# Use the official Python image as the base image
FROM python:3.10-slim

# Install missing system packages
RUN apt-get update && \
    apt-get install -y ffmpeg libsndfile1-dev

# Set the working directory inside the container
# Copy the application code and requirements file into the container
WORKDIR /workspace
ADD . /workspace

# Install the Python dependencies
RUN pip install -r requirements.txt

# Give correct access rights to the OVHcloud user
RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

# Set default values for 'model_id' & 'model_path' variables. Will be changable using --env parameter when launching AI Deploy app
ENV MODEL_ID="large-v3"
ENV MODEL_PATH="/workspace/whisper-model"

# Define the command to run the Streamlit application when the container is launched
CMD [ "streamlit" , "run" , "/workspace/app.py", "--server.address=0.0.0.0", "$MODEL_ID", "$MODEL_PATH"]
