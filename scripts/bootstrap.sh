#!/bin/bash -x
#
# bootstrap the environment
#

# set up the virtual env
python3.6 -m venv --prompt tempcontrol --clear env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# link the python-dev include directory in the venv
# (needed so boost-python will find pyconfig.h and build)
pushd env/include
INC=$(python3.6-config --includes | awk '{print $1}')
SRCDIR=${INC#"-I"}
DSTDIR=$(echo ${SRCDIR%"m"} | xargs basename)
ln -s ${SRCDIR} ${DSTDIR}
popd

# local boost install
./scripts/bootstrap_boost.sh

# now install the package into the virtualenv
./scripts/setup.sh
