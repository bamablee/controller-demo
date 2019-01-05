#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Interfaces to sensors
"""

# pylint: disable=bad-whitespace,invalid-name

from abc import abstractmethod
import itertools
import numpy as np

from . import NamedBase, _register # pylint: disable=cyclic-import

class SensorBase(NamedBase):
    """a named object with a read() method
    """
    @abstractmethod
    def read( self ):
        """Retrieve a measurement.
        """

class MockSensor(SensorBase):
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
_register( 'MockSensor', MockSensor )
