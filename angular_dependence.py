import math
import numpy as np
import os


def find_nearest_match_in_range_data(energy, path_range_data):
	data = np.loadtxt(path_range_data)
	energies = data[:, 0]
	idx = (np.abs(energies - energy)).argmin()
	return data[idx, 0], data[idx, 1], data[idx, 2], data[idx, 3]


def calculate_reduced_energy(energy, m_m, m_i, z_m, z_i):
	epsilon = energy * (m_m/(m_i + m_m)) * 0.03255/(z_i * z_m * np.sqrt(z_i**(2/3) + z_m**(2/3)))
	return epsilon


def initialize_file(path, theta):
	if os.path.exists(path):
		os.remove(path)
	f = open(path, 'w')
	f.write(f"Theta (deg):\n")
	f.write("===============================================================================================\n")
	for t in theta:
		f.write(f"{t:.2f}, ")
	f.write("\n")
	f.close()


def append_new_species_to_file(path, target_name, ion_name):
	f = open(path, 'a')
	f.write(f"Target: {target_name}, Ion: {ion_name}\n")
	f.write("===============================\n")
	f.close()


def append_angular_dependence_to_file(path, energy, a, alpha, beta, angular_probability):
	f = open(path, 'a')
	f.write(f"{energy}, ")
	f.write(f"{a}, ")
	f.write(f"{alpha}, ")
	f.write(f"{beta}, ")
	for ap in angular_probability:
		f.write(f"{ap:.10f}, ")
	f.write("\n")
	f.close()


def read_angular_data_from_file(path, target_name, ion_name):
	f = open(path, 'r')
	lines = f.readlines()
	in_block = False
	print("reading angular dependence from file")
	print("pair: ")
	print(f"Target: {target_name}, Ion: {ion_name}")
	theta = lines[2].strip().split(",")
	if theta[-1] == '':
		theta.pop(-1)
	theta = [float(x) for x in theta]

	angledata = [theta]  # theta line
	for line in lines:
		if f"Target: {target_name}, Ion: {ion_name}" in line:
			print("found target ion pair")
			in_block = True
			continue
		if in_block:
			if "============" in line:
				continue
			elif line == "" or "Target" in line:
				in_block = False
				break
			else:
				# turn string into list of floats
				line = line.strip().split(",")
				if line[-1] == '':
					line.pop(-1)
				line = [float(x) for x in line]
				angledata.append(line)
	f.close()
#	for a in angledata:
#		print(a)
	return angledata


def angdep(theta, a, alpha, beta, normalize=True):
	eta = np.cos(theta)
	eta_prime = np.sqrt(1-(eta**2))
	a_square = (alpha**2)*(eta**2) + (beta**2)*(eta_prime**2)

	y = (eta / np.sqrt(a_square)) * np.exp(-0.5*(eta**2)*(a**2)/a_square)

	if normalize:
		# y = y/np.sum(y)
		y = y * (1 / y[0])

	if np.isnan(y).any():
		print(a, alpha, beta)
		print(y)
		exit()
	return y


pi = math.pi
degtorad = pi/180
