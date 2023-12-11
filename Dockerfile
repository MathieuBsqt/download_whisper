# Base image to start from
FROM python:3.10

RUN apt-get update && \
    apt-get install -y ffmpeg libsndfile1-dev

WORKDIR /workspace
ADD requirements.txt /workspace

RUN pip install -r requirements.txt

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace
