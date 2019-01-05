#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#

import pytest
import time

@pytest.fixture
def blc():
    cfg = {
        'classname':'BoundedLinearController',
        'name':'ctrl1',
        'input_sel':'max',
        'in_lo':'25.0',
        'in_hi':'75.0',
        'out_lo':'20.0',
        'out_hi':'100.0',
        'cycle_secs':'0.1',
    }
    import tempcontrol
    return tempcontrol.factory(**cfg)

def test_name(blc):
    assert blc.name == 'ctrl1'

def test_in_lo(blc):
    assert blc.control_law( 24.0 ) == 20.0
    assert blc.control_law( 25.0 ) == 20.0

def test_in_hi(blc):
    assert blc.control_law( 75.0 ) == 100.0
    assert blc.control_law( 76.0 ) == 100.0

def test_in_mid(blc):
    assert blc.control_law( 50.0 ) == 60.0

def test_loop(blc):
    t0 = time.time()
    while blc.loop(5): continue
    elapsed = time.time() - t0

    assert blc.cycle == 5
    assert pytest.approx( elapsed, 0.01 ) == 0.5


    
