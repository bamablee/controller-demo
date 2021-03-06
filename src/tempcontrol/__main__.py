#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""provide 'python -m tempcontrol ...' invocation syntax
"""

# pylint: disable=bad-whitespace,invalid-name

import argparse
import configparser
import tempcontrol

def main():
    """Entry point for control-system invocation
    """
    # command-line parameters
    parser = argparse.ArgumentParser( prog='python -m tempcontrol',
                                      description='notional temperature-control system' )
    parser.add_argument( '-c', '--cfgfile', help='configuration file name' )
    parser.add_argument( '-n', '--ncycles', type=int, help='number of cycles to run' )
    parser.add_argument( '-o', '--outfile', help='archiver data file name' )
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

    # merge the archive filename from the command line to the config dictionary
    archiver_cfg = dict( cfg['archiver'].items() )
    archiver_cfg['fn'] = args.outfile

    # configure and run the controller
    with tempcontrol.factory( **archiver_cfg ) as archiver:
        controller.configure( sensors, actuators, archiver )
        controller.run( args.ncycles )

# entry point
main()
