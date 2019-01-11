# Conceptual Controller Framework

## Overview
This package demonstrates combining Python and C++ code using Boost::Python
in the context of a notional control-system framework. The framework is used
to compose control systems from configurable sensor, actuator, and controller
objects.  The state of the system is recorded by archiver objects.

## Requirements
This package expects to be run on a fairly modern Linux system with Python 3.6
and access to PyPI and the Boost project's download area. The code was developed
on a machine running Ubuntu 16.04 LTS with the python36, python36-dev,
python36-venv, g++, git and wget packages installed.

This package has also been run on a CentOS-6 system with the rh-python36 and
devtools-6 Software Collections packages installed and enabled.

## Getting Started
After cloning the project, run scripts/bootstrap.sh to set up the virtual
environment, and then run scripts/test.sh to build and deploy the framework
into the venv and run the unit tests.

Run scripts/demo1.sh to execute a control system described by the file
cfg/demo1.ini, save the results to a 'demo1.csv' data file, and then plot
the data.

Run scripts/demo2.sh to execute a control system described by the file
cfg/demo2.ini, save the results to a 'demo2.csv' data file, and then plot
the data.

## Container-based demo
If you have Docker available, you can run scripts/docker.sh to build and run
the demo configurations in an Ubuntu 18.04 container and copy the results back
to your host.
