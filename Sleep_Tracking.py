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
plt.axhline(y=1)

# Draw a default vline at x=1 that spans the yrange
plt.axvline(x=0)

# plt.plot(ms, X_Axis, "g")
plt.plot(ms, X_Axis, 'r', ms, Y_Axis, 'g')
plt.minorticks_on()
# plt.axis('tight')
plt.show()
# Print out Sensors
print(X_Axis)
