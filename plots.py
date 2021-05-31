import numpy as np
import matplotlib.pyplot as plt
from utilities.math_functions import *

def sequence():
    sequence = []
    i = 10
    while i <= int(1e6):
        sequence.append(i)
        increment = prev_power_of_ten(i)//10 if i < int(1e5) else prev_power_of_ten(i)
        i += increment

    return np.array(sequence)

def read_results_experiment(path_bs, path_veb):
    f_bs = open(path_bs, 'r')
    f_veb = open(path_veb, 'r')
    bs_times = []
    veb_times = []

    for line in f_bs.readlines():
        num = line.split('\n')[0]
        bs_times.append(float(num))
    f_bs.close()

    for line in f_veb.readlines():
        num = line.split('\n')[0]
        veb_times.append(float(num))
    f_veb.close()
    
    return np.array([bs_times, veb_times])

if __name__ == "__main__":

    nums_to_plot_0 = np.arange(10, 1010, 10)
    times_0 = read_results_experiment("texts/times_bs_0.txt", "texts/times_veb_0.txt")
    plt.plot(nums_to_plot_0, times_0[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_0, times_0[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()

    nums_to_plot_1 = np.arange(1000, 10100, 100)
    times_1 = read_results_experiment("texts/times_bs_1.txt", "texts/times_veb_1.txt")
    plt.plot(nums_to_plot_1, times_1[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_1, times_1[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()

    nums_to_plot_2 = np.arange(10000, 101000, 1000)
    times_2 = read_results_experiment("texts/times_bs_2.txt", "texts/times_veb_2.txt")
    plt.plot(nums_to_plot_2, times_2[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_2, times_2[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()

    nums_to_plot_3 = np.arange(100000, 1010000, 10000)
    times_3 = read_results_experiment("texts/times_bs_3.txt", "texts/times_veb_3.txt")
    plt.plot(nums_to_plot_3, times_3[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_3, times_3[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()
