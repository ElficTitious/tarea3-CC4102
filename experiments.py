
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

    time_data_experiment(path_file_bs, path_file_veb) 
    time_data_generation_0(path_file_bs_0, path_file_veb_0) 
    time_data_generation_1(path_file_bs_1, path_file_veb_1) 
    time_data_generation_2(path_file_bs_2, path_file_veb_2) 
    time_data_generation_3(path_file_bs_3, path_file_veb_3) 
    
