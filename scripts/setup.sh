#!/bin/bash -x
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
# wrapper script to invoke setup.py
#

# make sure to run in our venv
if [ -z ${VIRTUAL_ENV} ]; then
    source env/bin/activate
fi

# clean up existing build artifacts
rm -rf build dist *.egg-info

# now run setup.py to install into the venv
python setup.py install --prefix=$(pwd)/env

# clean up leftover build artifacts
rm -rf build dist *.egg-info
