# Import pandas as pd
import math
import pandas as pd
import matplotlib.pyplot as plt

# Import the AndroSensor.csv data: Sensors
data = pd.read_csv('AndroSensor.csv', sep=',')

X_Axis = data['X']
Y_Axis = data['Y']
Z_Axis = data['Z']

ms = data['ms']
date = data['Date']

# Draw a default hline at y=1 that spans the xrange
plt.axhline(y=0)

# Draw a default vline at x=1 that spans the yrange
plt.axvline(x=0)

plt.plot(ms, X_Axis, 'r', ms, Y_Axis, 'g', ms, Z_Axis, 'b')
plt.minorticks_on()
plt.title('Sleep Tracking ----- Movement vs Time ')
plt.legend((' = X',' = Y',' = Z'))
plt.show()
# Print out Sensors
minX = min(X_Axis)
maxX = max(X_Axis)

minY = min(Y_Axis)
maxY = max(Y_Axis)

minZ = min(Z_Axis)
maxZ = max(Z_Axis)

print('\n-----------------------------')
print('The min of the X Axis is %s.' % minX)
print('The max of the X Axis is %s.' % maxX)
print('\nThe min of the Y Axis is %s.' % minY)
print('The max of the Y Axis is %s.' % maxY)
print('\nThe min of the Z Axis is %s.' % minZ)
print('The max of the Z Axis is %s.' % maxZ)

seconds = ms / 1000
minSec = float(min(seconds))
maxSec = float(max(seconds))

print('\n*****************************')
print('The min time is %.2f' % minSec)
print('The max time is %.2f' % maxSec)
