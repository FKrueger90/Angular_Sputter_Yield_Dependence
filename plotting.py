from matplotlib import pyplot as plt

import numpy as np
import angular_dependence as angdep
import os
import math
from matplotlib import animation
# from matplotlib.animation import PillowWriter


dir_data = os.path.join(os.getcwd(), "Data")
path_data_angdep = os.path.join(dir_data, "Angular_Dependence_All")


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
    degtorad = math.pi / 180
    plt.figure()
    for energy in energies:
        e, a, alpha, beta = angdep.find_nearest_match_in_range_data(energy, rangedata_file)
        y = angdep.angdep(theta, a, alpha, beta, normalize=normalize)

        plt.plot(theta, y, label=f"{energy} eV")
        plt.xticks([0, degtorad * 15, degtorad * 30, math.pi / 4, degtorad * 60, degtorad * 75, math.pi / 2],
               ['0', '15', '30', '45', '60', '75', '90'])
    plt.legend()
    plt.savefig('angular_dependence.png')

    plt.close()


def check_output_folders():
    dir_figures = os.path.join(os.getcwd(), 'Figures')
    dir_animations = os.path.join(os.getcwd(), 'Animations')

    if not os.path.exists(dir_figures):
        os.makedirs(dir_figures)
    if not os.path.exists(dir_animations):
        os.makedirs(dir_animations)

    return dir_figures, dir_animations


def plot_angdep_movie(target_material, ion, path_data, dir_animations):

    angdep_data = angdep.read_angular_data_from_file(path_data, target_material, ion)

    theta = angdep_data[0]
    angdep_data.pop(0)
    name_file = f'angdep-{ion}-on-{target_material}-animation.GIF'
    path_file = os.path.join(dir_animations, name_file)
    fig = plt.figure()
    fig.suptitle(f'{ion} on {target_material}')
    ax = plt.axes(xlim=(0, 90), ylim=(0, 1.2))
    line, = ax.plot([], [], lw=2)
    text = ax.text(0.90, 1.1, "")

    plt.figure()
    for i in range(10):
        y = angdep_data[i][4:]
        plt.plot(theta, y)
    plt.show()

    def init():
        line.set_data([], [])
        return line,

    def animate(i):

        x = theta
        max_y = max(angdep_data[i][4:])
        y = [x / max_y for x in angdep_data[i][4:]]

        line.set_data(x, y)
        text.set_text(f"{round(angdep_data[i][0])} eV")
        return line, text,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=100, interval=200, blit=True)

    anim.save(name_file, writer=animation.PillowWriter(fps=10))


def plot_mcfpm_reference(num=0):

    mcfpm_theta = [0., 10., 20., 30., 40., 50., 60., 70., 80., 90.]
    mcfpm_angdeps = [
        [0.56, 0.58, 0.60, 0.58, 0.86, 1.30, 1.34, 1.00, 0.74, 0.00],
        [1.00, 1.00, 1.00, 1.00, 1.00, 0.90, 0.80, 0.60, 0.30, 0.00],
        [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.80, 0.60, 0.30, 0.00],
        [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.70, 0.40, 0.00],
        [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.60, 0.00],
        [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
        [1.00, 0.50, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
        [0.80, 0.83, 0.85, 0.83, 0.89, 1.30, 1.34, 1.00, 0.74, 0.00],
        [1.00, 1.00, 1.00, 1.00, 1.00, 0.90, 0.80, 0.60, 0.38, 0.10],
        [1.00, 1.00, 1.00, 1.00, 1.00, 0.90, 0.80, 0.60, 0.40, 0.20],
        [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.60, 0.20],
        [0.56, 0.58, 0.60, 0.58, 0.86, 1.30, 1.34, 1.20, 0.94, 0.50],
        [1.00, 1.00, 1.00, 1.00, 0.90, 0.80, 0.60, 0.30, 0.00, 0.00]]

    plt.figure()
    if num == 0:
        for mcfpm_angdep in mcfpm_angdeps:
            num = num + 1
            plt.plot(mcfpm_theta, mcfpm_angdep, label=f"{num}")

    else:
        if type(num) == int:
            nums = [num]
        for i in nums:
            plt.plot(mcfpm_theta, mcfpm_angdeps[i-1], label=f"{i}")
    plt.legend()
    plt.show()

    return [mcfpm_theta, mcfpm_angdeps]


set_plot_globals()
dir_figures, dir_animations = check_output_folders()

# plot_mcfpm_reference(1)

plot_angdep_movie("Si", "F", path_data_angdep, dir_animations)
