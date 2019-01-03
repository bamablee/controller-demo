#
# Copyright (c) 2018 Bryson Lee. All rights reserved.
#
"""Controller implementations
"""

from abc import abstractmethod
import time
import numpy as np

from . import named_base

class controller_base(named_base):
    def __init__( self, name=None, cycle_secs=0.0, **kwargs ):
        super().__init__( name )
        self.__cycle_secs = float(cycle_secs)
        self.__sensors = []
        self.__actuators = []
        self.__archiver = None
        self.__configured = False
        self.__cycle = 0

    @abstractmethod
    def configure( self, sensors, actuators, archiver=None, **kwargs ):
        self.__sensors = sensors
        self.__actuators = actuators
        self.__archiver = archiver
        self.__configured = True
        pass

    @abstractmethod
    def control_law( self, inputs ):
        pass

    @abstractmethod
    def run( self, cycles=-1 ):
        pass

    def loop( self, cycles=-1 ):
        """Loop control method

        This method is called from the run() method of concrete
        subclasses and provides timing and loop control.

        Args:
          cycles: number of cycles to execute. -1 means run forever

        Returns:
          True until the specified number of cycles have been executed,
          then False.

        """
        # bail if we've reached the cycle limit
        if self.__cycle >= cycles: return False

        # wait until the cycle time has elapsed, then increment the counter
        time.sleep( self.__cycle_secs )
        self.__cycle += 1

        # keep  the loop going
        return True

    @property
    def name( self ):
        return super().name

    @property
    def sensors( self ):
        return self.__sensors

    @property
    def actuators( self ):
        return self.__actuators

    @property
    def archiver( self ):
        return self.__archiver

    @property
    def configured( self ):
        return self.__configured

    @property
    def cycle( self ):
        return self.__cycle


class bounded_linear_controller( controller_base ):
    """Bounded linear proportional controller

    This controller interpolates feedforward control between
    lower and upper bounds, applying constant outputs when
    the input signal is outside those bounds.
    """
    def __init__( self, name=None, cycle_secs=0.0, input_sel=None,
                  in_lo=None, in_hi=None, out_lo=None, out_hi=None, **kwargs ):
        super().__init__( name, cycle_secs )
        if input_sel == 'max':
            self.__input_sel = max
        else:
            raise RuntimeError('unknown input selector "{}"'.format( input_sel ) )
        self.__x = (float(in_lo), float(in_hi))
        self.__y = (float(out_lo), float(out_hi))
        self.__state = [0.0, 0.0]


    def configure( self, sensors, actuators, archiver=None ):
        # call the base-class implementation
        super().configure( sensors, actuators, archiver )

        # configure the archiver if available
        if self.archiver:
            self.archiver.configure( abscissa_var = 'cycle',
                                     sensor_vars = [x.name for x in self.sensors],
                                     actuator_vars = [x.name for x in self.actuators],
                                     controller_vars = ['max_temp', 'pct_speed']
                                     )

    def control_law( self, inputs ):
        """Compute the output control signal based on the input signal
        """
        return np.interp( inputs, self.__x, self.__y )

    def run( self, cycles ):
        # write the initial state of the system to the archive
        if self.archiver:
            sens_ic = (x.read() for x in self.sensors)
            act_ic = (x.read() for x in self.actuators)
            self.archiver.write( abscissa = self.cycle,
                                 sensor_vals = sens_ic,
                                 actuator_vals = act_ic,
                                 controller_vals = self.__state
                                 )

        # now cycle the controller
        while self.loop( cycles ):
            # acquire the sensor inputs
            inputs = [x.read() for x in self.sensors]

            # execute the control law
            self.__state[0] = self.__input_sel( inputs )
            self.__state[1] = self.control_law( self.__state[0] )

            # drive the actuators and read back the results
            for a in self.actuators: a.write( self.__state[1] )
            outputs = [x.read() for x in self.actuators]

            # save the current state
            if self.archiver:
                self.archiver.write( abscissa = self.cycle,
                                     sensor_vals = inputs,
                                     actuator_vals = outputs,
                                     controller_vals = self.__state
                                     )

# install all configurable  types in the package registry
from . import registry
registry['bounded_linear_controller'] = bounded_linear_controller

