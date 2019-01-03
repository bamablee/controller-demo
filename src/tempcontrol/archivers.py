#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Data-archiver implementations
"""

from abc import abstractmethod
import csv
import itertools

from . import named_base

class archiver_base(named_base):
    """Define the methods required by concrete archiver implementations,
    and provide context-manager functionality.
    """
    def __init__( self, name=None, filename=None, **kwargs ):
        super().__init__( name )

    @property
    def name( self ):
        return super().name

    @abstractmethod
    def configure( self, abscissa_var, sensor_vars, actuator_vars, controller_vars ):
        pass

    @abstractmethod
    def write( self, abscissa_val, sensor_vals, actuator_vals, controller_vals ):
        pass

    @abstractmethod
    def open( self ):
        """called from context-manager __enter__() method
        """
        pass

    @abstractmethod
    def close( self ):
        """called from context-manager __exit__() method
        """
        pass

    def __enter__( self ):
        """Required method for context managers
        """
        return self.open()

    def __exit__( self, exc_type, exc_value, exc_traceback ):
        """Required method for context managers
        """
        self.close()

class file_archiver(archiver_base):
    def __init__( self, name=None, fn=None, **kwargs ):
        super().__init__( name )
        self.__fn = fn

    @property
    def filename( self ):
        return self.__fn


class csv_file_archiver(file_archiver):
    def __init__( self, name=None, fn=None, **kwargs ):
        super().__init__( name, fn )
        self.__fd = open( self.filename, 'w', newline='' )
        self.__csv = None

    def configure( self, abscissa_var, sensor_vars, actuator_vars, controller_vars ):
        self.__csv = csv.writer( self.__fd )
        self.__csv.writerow( itertools.chain( (abscissa_var, ),
                                              sensor_vars,
                                              actuator_vars,
                                              controller_vars ) )

    def write( self, abscissa, sensor_vals, actuator_vals, controller_vals ):
        self.__csv.writerow( itertools.chain( (abscissa, ),
                                              sensor_vals,
                                              actuator_vals,
                                              controller_vals ) )

    def open( self ):
        return self

    def close( self ):
        self.__fd.close()


# install all defined types in the package registry
from . import registry
registry['csv_file_archiver'] = csv_file_archiver

