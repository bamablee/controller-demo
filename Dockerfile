FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y g++ python3 python3-dev python3-venv wget git && \
    git clone https://github.com/bamablee/controller-demo.git && \
    cd controller-demo && \
    ./scripts/bootstrap.sh && \
    ./scripts/demo1.sh && \
    ./scripts/demo2.sh && \
    cd ..

