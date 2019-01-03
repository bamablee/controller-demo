#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Interfaces to sensors
"""

from abc import abstractmethod
import itertools
import numpy as np

from . import named_base

class sensor_base(named_base):
    """a named object with a read() method
    """
    def __init__( self, name=None, **kwargs ):
        super().__init__( name )

    @property
    def name( self ):
        return super().name

    @abstractmethod
    def read( self ):
        pass

class mock_sensor(sensor_base):
    """an object that returns a configurable 
    series of repeating values.
    """
    def __init__( self, name, min_val, max_val, nsteps, shape ):
        super().__init__( name )

        v0 = float(min_val)
        v1 = float(max_val)
        ns = int(nsteps)

        # create the sequence of values
        self.__values = None
        if shape == 'ramp':
            self.__values = np.linspace(v0, v1, ns)
        elif shape == 'sine':
            ampl = (v1 - v0) / 2.0
            ofst = v0 + ampl
            self.__values = ampl * np.sin(np.linspace(0.0, 2*np.pi, ns)) + ofst
        else:
            raise RuntimeError( 'unknown shape "%s"' % shape )

        # create an iterator over the value list
        self.__seq = itertools.cycle( self.__values )


    def read( self ):
        return next(self.__seq)

    @property
    def values( self ):
        """returns the underlying sequence from which measuremts are read.
        """
        return self.__values

# install all defined types in the package registry
from . import registry
registry['mock_sensor'] = mock_sensor
