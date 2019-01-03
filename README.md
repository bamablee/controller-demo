# Conceptual Controller Framework

## Overview
This package demonstrates combining Python and C++ code using Boost::Python
in the context of a notional control-system framework. The framework is used
to compose control systems from configurable sensor, actuator, and controller
objects.  The state of the system is recorded by archiver objects.

## Requirements
This package expects to be run on a fairly modern Linux system with Python 3.6
and access to PyPI and the Boost project's download area. The code was developed
on a machine running Ubuntu 16.04 LTS.

## Getting Started
After cloning the project, run scripts/bootstrap.sh to set up the virtual
environment, and then run scripts/test.sh to build and deploy the framework
into the venv and run the unit tests.

Run scripts/demo1.sh to execute a control system described by the file
cfg/demo1.ini and save the results to a 'demo1.csv' data file.
