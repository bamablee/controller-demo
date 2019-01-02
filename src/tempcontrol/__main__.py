#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""provide 'python -m tempcontrol ...' invocation syntax
"""

import argparse
import configparser
import tempcontrol

# command-line parameters
parser = argparse.ArgumentParser( prog='python -m tempcontrol',
                                  description='notional temperature-control system' )
parser.add_argument( '-c', '--cfgfile', help='configuration file name' )
parser.add_argument( '-n', '--ncycles', type=int, help='number of cycles to run' )
args = parser.parse_args()

# read the configuration file
cfg = configparser.ConfigParser()
cfg.read( args.cfgfile )

# instantiate the sensors
sensors = []
for s in (x for x in cfg.sections() if x.startswith('sensor')):
    sensors.append( tempcontrol.factory( **dict( cfg[s].items() ) ) )

# instantiate the actuators
actuators = []
for a in (x for x in cfg.sections()  if x.startswith('actuator')):
    actuators.append( tempcontrol.factory( **dict( cfg[a].items() ) ) )

# instantiate the controller
controller = tempcontrol.factory( **dict( cfg['controller'].items() ) )

# configure and run the controller
controller.configure( sensors, actuators )
controller.run( args.ncycles )


