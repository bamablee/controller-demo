#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Interfaces to actuators
"""

# pylint: disable=bad-whitespace,invalid-name,no-name-in-module,unused-import

from _tempcontrol_ext import pwm_fan, get_reg, set_reg

from . import _register # pylint: disable=cyclic-import

# create factory wrappers to coerce ctor arguments that come in as
# strings from config files into types suitable for C++
def _wrap_pwm_fan( **kwargs ):
    typed_kwargs = {
        'name': kwargs['name'],
        'pwm_max': int( kwargs['pwm_max'], base=0 ),
        'pwm_addr': int( kwargs['pwm_addr'], base=0 ),
        'rpm_max': float( kwargs['rpm_max'] ),
        }
    return pwm_fan( **typed_kwargs )

# install all config-file-instantiable types in the package registry
_register( 'PwmFan', _wrap_pwm_fan )
