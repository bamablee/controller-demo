#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""A Python package providing sensors, actuators, and
controllers for a notional temperature-regulation system.
"""

# pylint: disable=bad-whitespace,invalid-name

# package-level dictionary of class names to classes
__REGISTRY = {}
def _register( clsname, cls ):
    __REGISTRY[clsname] = cls

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
    if classname not in __REGISTRY.keys():
        raise RuntimeError('unknown object type {}'.format( classname ) )

    # create and return the instance
    cls = __REGISTRY[classname]
    return cls( name=name, **kwargs )

# define the root of an abstract mixin class hierarchy
# to control the interfaces to sensors, actuators, and controllers
class NamedBase:
    """every object in the system has to have a name and may
    have a parent
    """
    def __init__( self, name=None ):
        if not name:
            raise RuntimeError( 'instance name unspecified' )
        self.__name = name
        self.__parent = None

    @property
    def parent( self ):
        """cls: return the parent class"""
        return self.__parent

    @parent.setter
    def parent( self, p ):
        self.__parent = p

    @property
    def name( self ):
        """str: return the (possibly hierarchical) name"""
        name = ''
        if self.__parent is not None:
            name += self.__parent.name + '.'
        name += self.__name
        return name

#pylint: disable=wrong-import-position
# bring modules into the package namespace
from . import sensors
from . import actuators
from . import controllers
from . import archivers
