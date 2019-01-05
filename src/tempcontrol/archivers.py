#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Data-archiver implementations
"""

# pylint: disable=bad-whitespace,invalid-name

from abc import abstractmethod
import csv
import itertools

from . import NamedBase, _register  # pylint: disable=cyclic-import

class ArchiverBase(NamedBase):
    """Define the methods required by concrete archiver implementations,
    and provide context-manager functionality.
    """
    @abstractmethod
    def configure( self, abscissa_var, sensor_vars, actuator_vars, controller_vars ):
        """Provides parameter names as storage meta-data
        """

    @abstractmethod
    def write( self, abscissa_val, sensor_vals, actuator_vals, controller_vals ):
        """Write a data record to the archive
        """

    @abstractmethod
    def open( self ):
        """called from context-manager __enter__() method
        """

    @abstractmethod
    def close( self ):
        """called from context-manager __exit__() method
        """

    def __enter__( self ):
        """Required method for context managers
        """
        return self.open()

    def __exit__( self, exc_type, exc_value, exc_traceback ):
        """Required method for context managers
        """
        self.close()

class FileArchiver(ArchiverBase):
    """Superclass for file-based archivers
    """
    #pylint: disable=W0223
    def __init__( self, name=None, fn=None ):
        super().__init__( name )
        self.__fn = fn

    @property
    def filename( self ):
        """str: archive file name"""
        return self.__fn


class CsvFileArchiver(FileArchiver):
    """Store data to a CSV file.
    """
    def __init__( self, name=None, fn=None ):
        super().__init__( name, fn )
        self.__fd = open( self.filename, 'w', newline='' )
        self.__csv = None

    def configure( self, abscissa_var, sensor_vars, actuator_vars, controller_vars ):
        self.__csv = csv.writer( self.__fd )
        self.__csv.writerow( itertools.chain( (abscissa_var, ),
                                              sensor_vars,
                                              actuator_vars,
                                              controller_vars ) )

    def write( self, abscissa_val, sensor_vals, actuator_vals, controller_vals ):
        self.__csv.writerow( itertools.chain( (abscissa_val, ),
                                              sensor_vals,
                                              actuator_vals,
                                              controller_vals ) )

    def open( self ):
        return self

    def close( self ):
        self.__fd.close()


# install all defined types in the package registry
_register('CsvFileArchiver', CsvFileArchiver)
