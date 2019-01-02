#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""A Python package providing sensors, actuators, and
controllers for a notional temperature-regulation system.
"""

import logging
logger = logging.getLogger( __name__ )

# package-level dictionary of class names to classes
registry = {}

# define the root of an abstract mixin class hierarchy
# to control the interfaces to sensors, actuators, and controllers
from abc import ABC, abstractmethod

class named_base(ABC):
    """every object in the system has to have a name
    """
    def __init__( self, name=None, **kwargs ):
        if not name:
            raise runtime_error( 'instance name unspecified' )
        self.__name = name

    @property
    @abstractmethod
    def name( self ):
        return self.__name


# bring modules into the package namespace
from . import sensors
from . import actuators
from . import controllers

# implement a factory for instantiating/configuring elements of the system
def factory( name=None, classname=None, **kwargs ):
    """Factory function for module objects

    Args:
      name: instance name
      classname: object type, must be one of the defined/registered object types
      kwargs: arguments to be passed to the object ctor

    Returns:
      an instance of the specified class
    """
    # validate inputs
    if not name:
        raise RuntimeError('missing object name')
    if not classname:
        raise RuntimeError('missing class name')
    if classname not in registry.keys():
        raise RuntimeError('unknown object type {}'.format( classname ) )

    # create and return the instance
    inst = None
    try:
        logger.debug( 'creating object {} as {} with kwargs {}'.format( name, classname, kwargs ) )
        klass = registry[classname]
        inst = klass( name=name, **kwargs )
    except Exception as e:
        logger.error( '{}: {}'.format( e.__class__.__name__, str(e) ) )
        logger.error( 'failed to instantiate {} as {}'.format( name, classname ) )
        raise
    return inst


