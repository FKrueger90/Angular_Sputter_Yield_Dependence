import matplotlib.pyplot as plt
import math
import numpy as np

def set_plot_globals():
    """
    sets global plotting presets
    """
    plt.style.use('classic')
    plt.rcParams['agg.path.chunksize'] = 10000
    plt.rcParams['font.size'] = 16
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.top"] = True
    plt.rcParams["ytick.right"] = True
    # plot legend
    plt.rcParams['legend.fontsize'] = 'small'
    plt.rcParams['legend.loc'] = 'best'

def calculate_reduced_energy(energy, m_m, m_i, z_m, z_i):
	epsilon = energy * (m_m/(m_i + m_m)) * 0.03255/(z_i * z_m * np.sqrt(z_i**(2/3) + z_m**(2/3)))
	return epsilon

test = calculate_reduced_energy(1000, 28, 39, 14, 18)

print(test)

exit()


set_plot_globals()

pi = math.pi

theta = np.linspace(0, math.pi/2, 100)
degtorad = pi/180

def angdep(theta, a , alpha, beta, normalize=True):
	Asquare =  (alpha*np.cos(theta)**2 + beta*np.sin(theta))
	factor = 0.5 * (a**2 / Asquare) 
	y = np.cos(theta)*np.exp(factor*(np.sin(theta)**2))
	if normalize:
		y = y/np.sum(y) 
	return y

# variation of a 
#-------------------------------------------------------------------
a_list = [1, 2, 3, 4, 5]
maxima = []
for a in a_list:
	
	alpha = a/2.5
	beta = a/1.5

	y = angdep(theta, a , alpha, beta, normalize=False)
	max_index =np.argmax(y)
	maxima.append((theta[max_index], y[max_index]))
	plt.plot(theta, y)

plt.xticks([0, degtorad*15, degtorad*30, pi/4,degtorad*60, degtorad*75, pi/2], ['0', '15', '30', '45', '60', '75', '90'])
plt.plot(*zip(*maxima), "--")
plt.savefig('a_var.png')
plt.close()

# variation of alpha=beta, a=4
#-------------------------------------------------------------------
ratio_list = [2, 3, 4, 5]
maxima = []
for ratio in ratio_list:
	a = 2
	alpha = a/ratio
	beta = a/ratio

	y = angdep(theta, a , alpha, beta, normalize=False)
	max_index =np.argmax(y)
	maxima.append((theta[max_index], y[max_index]))
	plt.plot(theta, y)

plt.xticks([0, degtorad*15, degtorad*30, pi/4,degtorad*60, degtorad*75, pi/2], ['0', '15', '30', '45', '60', '75', '90'])
plt.plot(*zip(*maxima), "--")
plt.savefig('alpha_var.png')
plt.close()