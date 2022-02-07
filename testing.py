import numpy as np
import matplotlib.pyplot as plt
import math
import angular_dependence as angdep

degtorad = angdep.degtorad
pi = math.pi
theta = np.linspace(0, math.pi/2, 100)


# reference testing
yC = angdep(theta, 18, 8, 10, normalize=True)
plt.plot(theta, yC)
#yXe = angdep(theta, 17, 8, 9, normalize=True)
#plt.plot(theta, yXe)
#yKr = angdep(theta, 11, 6, 4, normalize=True)
#plt.plot(theta, yKr)
#yNe = angdep(theta, 16, 9, 6, normalize=True)
#plt.plot(theta, yNe)

#yAg = angdep(theta, 156, 59, 35, normalize=True)
#plt.plot(theta, yAg)

plt.xticks([0, degtorad*15, degtorad*30, pi/4, degtorad*60, degtorad*75, pi/2], ['0', '15', '30', '45', '60', '75', '90'])

plt.savefig('ref_test.png')
plt.show()
plt.close()
