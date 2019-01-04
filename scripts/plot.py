#!/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt( sys.argv[1], delimiter=',', names=True )

x = data['cycle']
y1 = [data[s] for s in data.dtype.names if s.startswith('sensor')]
y2 = [data[a] for a in data.dtype.names if a.startswith('actuator')]

plt.figure(1)
plt.plot( x, np.transpose(y1) )
plt.title( 'Sensor Inputs' )
plt.figure(2)
plt.plot( x, np.transpose(y2) )
plt.title( 'Actuator Outputs' )
plt.figure(3)
plt.plot( x, data['max_temp'], label='max_temp' )
plt.plot( x, data['pct_speed'], label='pct_speed' )
plt.title( 'Controller State' )
plt.legend()
plt.show()

                      


