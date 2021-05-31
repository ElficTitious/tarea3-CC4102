"""This script holds the execution of the experiments.
We put them in a separate script because they are computationally
expensive. This script overwrites the .txt files in the texts directory.
"""

from utilities.data_generation import *

if __name__ == "__main__":
    
    path_file_bs = "texts/times_bs.txt"
    path_file_veb = "texts/times_veb.txt"

    path_file_bs_0 = "texts/times_bs_0.txt"
    path_file_veb_0 = "texts/times_veb_0.txt"

    path_file_bs_1 = "texts/times_bs_1.txt"
    path_file_veb_1 = "texts/times_veb_1.txt"

    path_file_bs_2 = "texts/times_bs_2.txt"
    path_file_veb_2 = "texts/times_veb_2.txt"

    path_file_bs_3 = "texts/times_bs_3.txt"
    path_file_veb_3 = "texts/times_veb_3.txt"

    time_experiment(path_file_bs, path_file_veb) 
    time_data_generation(path_file_bs_0, path_file_veb_0, 10, 1000, 10) 
    time_data_generation(path_file_bs_1, path_file_veb_1, int(1e3), int(1e4), 100) 
    time_data_generation(path_file_bs_2, path_file_veb_2, int(1e4), int(1e5), 1000) 
    time_data_generation(path_file_bs_3, path_file_veb_3, int(1e5), int(1e6), 10000) 
    
