#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Interfaces to sensors
"""

import itertools
import math

class mock_sensor:
    """an object with a read() method that returns a configurable 
    series of repeating values.
    """
    def __init__( self, name, min_val, max_val, nsteps, shape ):

        self.__name = name

        # create the list of values
        self.__values = None
        if shape == 'ramp':
            sf = (max_val - min_val)/nsteps
            self.__values = tuple(x*sf+min_val for x in range(nsteps+1))
        elif shape == 'sine':
            sf = (max_val - min_val) / 2
            self.__values = tuple(math.sin(x*2*math.pi/nsteps)*sf+min_val+sf for x in range(nsteps+1))

        # create an iterator over the value list
        if self.__values:
            self.__seq = itertools.cycle( self.__values )
        else:
            raise RuntimeError( 'unknown shape "%s"' % shape )

    def read( self ):
        return next(self.__seq)

    @property
    def name( self ):
        return self.__name

    @property
    def values( self ):
        return self.__values

# install all defined types in the package registry
from . import registry
registry['mock_sensor'] = mock_sensor
