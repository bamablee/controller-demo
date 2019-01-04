#!/bin/bash -x
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
# wrapper script to run a controller demo
#

# make sure to run in our venv
if [ -z ${VIRTUAL_ENV} ]; then
    source env/bin/activate
fi

# run the demo
python -m tempcontrol -c cfg/demo2.ini -n 2000 -o demo2.csv

# plot the results
python scripts/plot.py demo2.csv

