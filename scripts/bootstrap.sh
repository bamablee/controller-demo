#!/bin/bash -x
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
# bootstrap the environment
#

# set up the virtual env
python3.6 -m venv --prompt tempcontrol --clear env
source env/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt

# link the python-dev include directory in the venv
# (needed so boost-python will find pyconfig.h and build)
pushd env/include
INC=$(python3.6-config --includes | awk '{print $1}')
SRCDIR=${INC#"-I"}
DSTDIR=$(echo ${SRCDIR%"m"} | xargs basename)
ln -s ${SRCDIR} ${DSTDIR}
popd

# install a local copy of Boost::Python
./scripts/install_boost_python.sh

# now install the package into the virtualenv
./scripts/setup.sh
