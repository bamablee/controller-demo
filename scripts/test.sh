#!/bin/bash -x
#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
# wrapper script to invoke pytest
#

# make sure to run in our venv
if [ -z ${VIRTUAL_ENV} ]; then
    source env/bin/activate
fi

# make sure the latest code is installed
./scripts/setup.sh >/dev/null

# run pylint on the codebase
pylint tempcontrol

# now run all the tests and generate an XUnit result file
pytest -v --junit-xml=pytest.xml tests/
