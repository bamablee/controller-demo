#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#

import pytest

# create wrappers for direct and factory-based instantiation of the C++
# pwm_fan object, to confirm that the argument-type-conversion wrapper
# works as expected
def direct_pwm_fan():
    import tempcontrol
    return tempcontrol.actuators.pwm_fan( 'fan1', 0x0000FFFF, 0xD0000001, 1000.0 )

def factory_pwm_fan():
    cfg = {
        'classname':'PwmFan',
        'name':'fan1',
        'pwm_max':'0x0000FFFF',
        'pwm_addr':'0xD0000001',
        'rpm_max':'1000.0',
    }
    import tempcontrol
    return tempcontrol.factory(**cfg)

# create a parameterized fixture for testing both instantiation techniques
@pytest.fixture( scope='module', params=[direct_pwm_fan, factory_pwm_fan] )
def pwm_fan( request ):
    return request.param()

def test_name(pwm_fan):
    assert pwm_fan.name == 'fan1'

def test_initial_speed(pwm_fan):
    assert pwm_fan.read() == 0.0

def test_set_speed(pwm_fan):
    pwm_fan.write( 25.0 )
    assert pytest.approx( pwm_fan.read(), 0.01 ) == 250.0

    pwm_fan.write( 50.0 )
    assert pytest.approx( pwm_fan.read(), 0.01 ) == 500.0

    pwm_fan.write( 75.0 )
    assert pytest.approx( pwm_fan.read(), 0.01 ) == 750.0

    pwm_fan.write( 100.0 )
    assert pytest.approx( pwm_fan.read(), 0.01 ) == 1000.0

def test_set_speed_exception(pwm_fan):
    with pytest.raises(Exception) as e_info:
        pwm_fan.write( 120.0 )

def test_pwm_register(pwm_fan):
    import tempcontrol
    pwm_fan.write( 50.0 )
    assert tempcontrol.actuators.get_reg( 0xD0000001 ) == 32768

def test_set_reg():
    import tempcontrol
    tempcontrol.actuators.set_reg( 0xD0000000, 0x55555555 )
    tempcontrol.actuators.set_reg( 0xD00003FF, 0xAAAAAAAA )
    assert True

def test_get_reg():
    import tempcontrol
    assert tempcontrol.actuators.get_reg( 0xD0000000 ) == 0x55555555
    assert tempcontrol.actuators.get_reg( 0xD00003FF ) == 0xAAAAAAAA

def test_reg_exception():
    import tempcontrol
    with pytest.raises(Exception) as e_info:
        tempcontrol.actuators.get_reg( 0xD0000400 )
