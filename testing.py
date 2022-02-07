import numpy as np
import matplotlib.pyplot as plt
import math
import angular_dependence as angdep

degtorad = angdep.degtorad
pi = math.pi
theta = np.linspace(0, math.pi/2, 100)

figsize = (8,5)
# reference testing
plt.figure(figsize=figsize, dpi=300)
yC = angdep.angdep(theta, 18, 8, 10, normalize=True)
plt.plot(theta, yC)
plt.xticks([0, degtorad*15, degtorad*30, pi/4, degtorad*60, degtorad*75, pi/2], ['0', '15', '30', '45', '60', '75', '90'])

plt.savefig('ref_test_diamond.png')
plt.show()
plt.close()

plt.figure(figsize=figsize, dpi=300)
yXe = angdep.angdep(theta, 17, 8, 9, normalize=True)
plt.plot(theta, yXe)
yKr = angdep.angdep(theta, 11, 6, 4, normalize=True)
plt.plot(theta, yKr)
yNe = angdep.angdep(theta, 16, 9, 6, normalize=True)
plt.plot(theta, yNe)
plt.savefig('ref_test_CU.png')
plt.show()
plt.close()

plt.figure(figsize=figsize, dpi=300)
yAg = angdep.angdep(theta, 156, 59, 35, normalize=True)
plt.plot(theta, yAg)
plt.savefig('ref_test_Ag.png')
plt.show()
plt.close()

