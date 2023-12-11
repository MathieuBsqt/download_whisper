WORKDIR /workspace
ADD requirements.txt /workspace

RUN pip install -r requirements.txt

RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace
