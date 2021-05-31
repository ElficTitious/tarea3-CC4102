import numpy as np
import matplotlib.pyplot as plt
from utilities.math_functions import *


def read_results_experiment(path_bs, path_veb):
    """Method used for reading the results of the experiments
    ran in experiments.py, and returns them as arrays.

    Parameters
    ----------
    path_bs : [str] Path of the file for the binary search results 
    path_veb : [str] Path of the file for the vEB Tree results 

    Returns
    -------
    results : [np.ndarray] Array with the results for each method. results[0]
              holds the results for binary search and results[1] holds the results for
              vEB Tree is_member().
    """
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
    results = np.array([bs_times, veb_times])

    return results 

if __name__ == "__main__":

    #=================== Plot for the range [10, 1000] ====================

    nums_to_plot_0 = np.arange(10, 1010, 10)
    times_0 = read_results_experiment("texts/times_bs_0.txt", "texts/times_veb_0.txt")
    plt.plot(nums_to_plot_0, times_0[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_0, times_0[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()

    #=================== Plot for the range [1e3, 1e4] ====================

    nums_to_plot_1 = np.arange(1000, 10100, 100)
    times_1 = read_results_experiment("texts/times_bs_1.txt", "texts/times_veb_1.txt")
    plt.plot(nums_to_plot_1, times_1[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_1, times_1[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()

    #=================== Plot for the range [1e4, 1e5] ====================

    nums_to_plot_2 = np.arange(10000, 101000, 1000)
    times_2 = read_results_experiment("texts/times_bs_2.txt", "texts/times_veb_2.txt")
    plt.plot(nums_to_plot_2, times_2[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_2, times_2[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()

    #=================== Plot for the range [1e5, 1e6] ====================

    nums_to_plot_3 = np.arange(100000, 1010000, 10000)
    times_3 = read_results_experiment("texts/times_bs_3.txt", "texts/times_veb_3.txt")
    plt.plot(nums_to_plot_3, times_3[0], label="Tiempo para búsqueda binaria")
    plt.plot(nums_to_plot_3, times_3[1], label="Tiempo para vEB Tree")
    plt.xlabel("Número de elementos en arreglo", fontsize=12)
    plt.ylabel("Tiempo (ms)", fontsize=12)
    plt.legend()
    plt.show()
