#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""A Python module providing sensors, actuators, and
controllers for a notional temperature-regulation system.
"""

import logging
logger = logging.getLogger( __name__ )

# package-level dictionary of class names to classes
registry = {}

# import modules
from . import sensors
from . import actuators
from . import controllers

# implement a factory for instantiating/configuring
# elements of the system
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

# provide "python -m tempcontrol ..." invocation syntax
if __name__ == '__main__':
    import argparse
    import configparser

    # command-line parameters
    parser = argparse.ArgumentParser( prog='python -m tempcontrol',
                                      description='notional temperature-control system' )
    parser.add_argument( '-c', '--cfg', help='configuration file name' )
    parser.add_argument( '-s', '--sec', help='run time in seconds' )
    args = parser.parse_args()

    # read the configuration file
    cfg = configparser.ConfigParser()
    cfg.read( args.cfg )
