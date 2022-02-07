from matplotlib import pyplot as plt
import numpy as np
from angular_dependence import *


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


def plot_range(rangedata_files):
    plt.figure()
    for file in rangedata_files:
        label = file[5:-10]
        data = np.loadtxt(file)
        plt.plot(data[:, 0], data[:, 1], label=label)
    plt.xlim(100, 50000)
    plt.ylim(0.3, 100)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("incident energy (eV)")
    plt.ylabel("range (nm)")
    plt.legend()
    plt.savefig('ranges.png')
    plt.close()


def plot_angular_dependence(rangedata_file, energies, normalize=True):
    theta = np.linspace(0, math.pi / 2, 100)
    degtorad = pi / 180
    plt.figure()
    for energy in energies:
        e, a, alpha, beta = find_nearest_match_in_range_data(energy, rangedata_file)
        y = angdep(theta, a, alpha, beta, normalize=normalize)

        plt.plot(theta, y, label=f"{energy} eV")
        plt.xticks([0, degtorad * 15, degtorad * 30, pi / 4, degtorad * 60, degtorad * 75, pi / 2],
               ['0', '15', '30', '45', '60', '75', '90'])
    plt.legend()
    plt.savefig('angular_dependence.png')

    plt.close()


set_plot_globals()

files_range = [
    "Data\\Ar---Si.rangedata",
    "Data\\Ar---SiO2.rangedata",
    "Data\\Ar---Si3N4.rangedata",
    "Data\\Ar---HfO2.rangedata"
]
energies = [100, 500, 1000 ]
plot_angular_dependence("Data\\Ar---SiO2.rangedata", energies, normalize=True)

plot_range(files_range)



# variation of a
# -------------------------------------------------------------------
a_list = [1, 2, 3, 4, 5]
maxima = []
for a in a_list:
    alpha = a / 2.5
    beta = a / 1.5

    y = angdep(theta, a, alpha, beta, normalize=False)
    max_index = np.argmax(y)
    maxima.append((theta[max_index], y[max_index]))
    plt.plot(theta, y)

plt.xticks([0, degtorad * 15, degtorad * 30, pi / 4, degtorad * 60, degtorad * 75, pi / 2],
           ['0', '15', '30', '45', '60', '75', '90'])
plt.plot(*zip(*maxima), "--")
plt.savefig('a_var.png')
plt.close()

# variation of alpha=beta, a=4
# -------------------------------------------------------------------
ratio_list = [2, 3, 4, 5]
maxima = []
for ratio in ratio_list:
    a = 2
    alpha = a / ratio
    beta = a / ratio

    y = angdep(theta, a, alpha, beta, normalize=False)
    max_index = np.argmax(y)
    maxima.append((theta[max_index], y[max_index]))
    plt.plot(theta, y)

plt.xticks([0, degtorad * 15, degtorad * 30, pi / 4, degtorad * 60, degtorad * 75, pi / 2],
           ['0', '15', '30', '45', '60', '75', '90'])
plt.plot(*zip(*maxima), "--")
plt.savefig('alpha_var.png')
plt.close()
