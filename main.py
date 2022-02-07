import os
import periodictable as pt
import srim_controller as srim
import angular_dependence as angdep
import numpy as np
import math

# Script start
# ==================================================================================================================
dir_data = os.path.join(os.getcwd(), "Data")
path_data_range = os.path.join(dir_data, "Range_Data_All")
srim.initialize_data_file(path_data_range)

# angle_bins
theta = np.linspace(0, math.pi/2, 91)
path_data_angdep = os.path.join(dir_data, "Angular_Dependence_All")
angdep.initialize_file(path_data_angdep, theta/angdep.degtorad)

targets = ["Cu", "Ag", "SiO2", "Si", "Si3N4", "GaAs", "Ge", "HfO2", "C"]
for target_material in targets:

    for ion_obj in pt.elements:
        ion_name = ion_obj.symbol
        # skip first element 'n'
        if ion_name == "n":
            continue
        if ion_name == "Np":
            break

        # generate range data using SRIM
        data = srim.run(ion_name, target_material)

        # append header to data file
        srim.append_to_data_file(path_data_range, data, target_material, ion_name)

        angdep.append_new_species_to_file(path_data_angdep, target_material, ion_name)

        for e in data:
            energy, a, alpha, beta = e
            ang_prob = angdep.angdep(theta, a, alpha, beta, normalize=True)
            angdep.append_angular_dependence_to_file(path_data_angdep, energy, a, alpha, beta, ang_prob)
