#!/bin/bash -x
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
# install a local copy of Boost::Python
#

# make sure to run in our venv
if [ -z ${VIRTUAL_ENV} ]; then
    source env/bin/activate
fi

# download boost
BOOST_VERSION=1_69_0
BOOST_DIRNAME=boost_${BOOST_VERSION}
BOOST_TARBALL=${BOOST_DIRNAME}.tar.bz2
BOOST_VERSION_DOTTED=$(echo $BOOST_VERSION | tr _ .)
BOOST_TARBALL_URL=https://dl.bintray.com/boostorg/release/${BOOST_VERSION_DOTTED}/source/${BOOST_TARBALL}
if [ ! -f /tmp/${BOOST_TARBALL} ]; then
    wget -O /tmp/${BOOST_TARBALL} ${BOOST_TARBALL_URL}
fi

# build boost
rm -rf ${BOOST_DIRNAME}
tar jxf /tmp/${BOOST_TARBALL}
pushd ${BOOST_DIRNAME}
./bootstrap.sh --with-libraries=python
./b2 install --prefix=../env
popd
rm -rf ${BOOST_DIRNAME}


