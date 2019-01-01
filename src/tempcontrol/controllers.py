#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Controller implementations
"""

import numpy as np

class bounded_linear_controller:
    """Bounded linear proportional controller

    This controller interpolates proportional control between
    lower and upper bounds, applying constant outputs when
    the input signal is outside those bounds.
    """
    def __init__( self, name=None, input_sel=None, in_lo=None, in_hi=None, out_lo=None, out_hi=None, **kwargs ):
        self.__name = name
        if input_sel == 'max':
            self.__input_sel = np.max
        else:
            raise RuntimeError('unknown input selector "{}"'.format( input_sel ) )
        self.__x = (float(in_lo), float(in_hi))
        self.__y = (float(out_lo), float(out_hi))
        self.__sensors = []
        self.__actuators = []
        self.__archiver = None
        self.__input_signal = 0.0
        self.__output_signal = 0.0

    def configure( self, sensors, actuators, archiver=None ):
        self.__sensors = sensors
        self.__actuators = actuators
        self.__archiver = archiver

    def control_law( self, input_signal ):
        """Compute the output control signal based on the input signal
        """
        return np.interp( input_signal, self.__x, self.__y )

    @property
    def name( self ):
        return self.__name
            

# install all configurable  types in the package registry
from . import registry
registry['bounded_linear_controller'] = bounded_linear_controller

