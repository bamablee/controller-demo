#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Interfaces to actuators
"""

from _tempcontrol_ext import pwm_fan, get_reg, set_reg

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
from . import registry
registry['pwm_fan'] = _wrap_pwm_fan
