# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Import the AndroSensor.csv DATA: Sensors
DATA = pd.read_csv('AndroSensor.csv', sep=',')

X_AXIS = DATA['X']
Y_AXIS = DATA['Y']
Z_AXIS = DATA['Z']

MS = DATA['ms']
DATE = DATA['Date']

# Draw a default hline at y=1 that spans the xrange
plt.axhline(y=0)

# Draw a default vline at x=1 that spans the yrange
plt.axvline(x=0)

plt.plot(MS, X_AXIS, 'r', MS, Y_AXIS, 'g', MS, Z_AXIS, 'b')
plt.minorticks_on()
plt.title('Sleep Tracking ----- Movement vs Time ')
plt.legend((' = X', ' = Y', ' = Z'))
plt.show()
# Print out Sensors
MINX = min(X_AXIS)
MAXX = max(X_AXIS)
AVGX = statistics.mean(X_AXIS)

MINY = min(Y_AXIS)
MAXY = max(Y_AXIS)
AVGY = statistics.mean(Y_AXIS)

MINZ = min(Z_AXIS)
MAXZ = max(Z_AXIS)
AVGZ = statistics.mean(Z_AXIS)

print('\n-----------------------------------')
print('The min of the X Axis is %s.' % MINX)
print('The max of the X Axis is %s.' % MAXX)
print('The average of the X Axis is %.2f.' % AVGX)

print('\nThe min of the Y Axis is %s.' % MINY)
print('The max of the Y Axis is %s.' % MAXY)
print('The average of the Y Axis is %.2f.' % AVGY)

print('\nThe min of the Z Axis is %s.' % MINZ)
print('The max of the Z Axis is %s.' % MAXZ)
print('The average of the Z Axis is %.2f.' % AVGZ)

SECONDS = MS / 1000
MINSEC = float(min(SECONDS))
MAXSEC = float(max(SECONDS))

print('\n**********************************')
print('The min time is %.2f' % MINSEC)
print('The max time is %.2f' % MAXSEC)
