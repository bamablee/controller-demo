#!/bin/bash -x
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
# wrapper script to invoke pytest
#

docker build -t controller-demo .
id=$(docker create controller-demo)
for f in demo1.csv demo1-fig1.png demo1-fig2.png demo1-fig3.png demo2.csv demo2-fig1.png demo2-fig2.png demo2-fig3.png; do
    docker cp $id:/controller-demo/$f .
done
docker rm -v $id
