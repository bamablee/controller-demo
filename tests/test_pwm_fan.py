# test PWM_Fan functionality
import pytest

@pytest.fixture
def pwm_fan():
    import tempcontrol
    return tempcontrol.actuators.PWM_Fan('fan1', 0x0000FFFF, 0xD0000001, 1000.0)

def test_name(pwm_fan):
    assert pwm_fan.name == 'fan1'

def test_initial_speed(pwm_fan):
    assert pwm_fan.speed == 0.0

def test_set_speed(pwm_fan):
    pwm_fan.set_speed( 25.0 )
    assert pytest.approx( pwm_fan.speed, 0.01 ) == 250.0

    pwm_fan.set_speed( 50.0 )
    assert pytest.approx( pwm_fan.speed, 0.01 ) == 500.0

    pwm_fan.set_speed( 75.0 )
    assert pytest.approx( pwm_fan.speed, 0.01 ) == 750.0

    pwm_fan.set_speed( 100.0 )
    assert pytest.approx( pwm_fan.speed, 0.01 ) == 1000.0

def test_set_speed_exception(pwm_fan):
    with pytest.raises(Exception) as e_info:
        pwm_fan.set_speed( 120.0 )

