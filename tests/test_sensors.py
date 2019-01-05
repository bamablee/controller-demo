#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#

import pytest

@pytest.fixture
def ramp():
    cfg = {
        'classname': 'MockSensor',
        'name': 'ramp',
        'min_val': '0.0',
        'max_val': '100.0',
        'nsteps': '100',
        'shape': 'ramp'
        }
    import tempcontrol
    return tempcontrol.factory(**cfg)

@pytest.fixture
def sine():
    cfg = {
        'classname': 'mock_sensor',
        'name': 'sine',
        'min_val': '0.0',
        'max_val': '100.0',
        'nsteps': '100',
        'shape': 'ramp'
        }
    import tempcontrol
    return tempcontrol.factory(**cfg)

def test_name(ramp):
    assert ramp.name == 'ramp'

def test_min(ramp):
    assert ramp.read() == 0

def test_mid(ramp):
    for i in range(49): ramp.read()
    assert pytest.approx( ramp.read(), .1 ) == 50.0

def test_max(ramp):
    for i in range(99): ramp.read()
    assert ramp.read() == 100.0

def test_cycle(ramp):
    for i in range(100): ramp.read()
    assert ramp.read() == 0.0
    

    
