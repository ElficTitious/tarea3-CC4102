
from utilities.data_generation import *

if __name__ == "__main__":
    
    path_file_bs = "../texts/times_bs.txt"
    path_file_veb = "../texts/times_veb.txt"

    time_data_generation(int(1e7), path_file_bs, path_file_veb) 
