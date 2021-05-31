
import numpy as np
from timeit import timeit
from algorithms.binary_search import *
from algorithms.static_veb_tree import StaticVEBTree
from utilities.math_functions import *
from random import *
from math import *
from utilities.timer import *

def data_generator(N):
    """Method for generating a sorted list of N random numbers.

    Parameters
    ----------
    N : [int] Number of elements to consider in the sorted random list.

    Returns
    -------
    temp_list : [list] Sorted list of N random numbers.
    """
    lower_bound = 0
    temp_list = []
    for i in range(N):
        rand_num = randint(lower_bound, lower_bound + 10)
        temp_list.append(rand_num)
        lower_bound = rand_num + 1
    return temp_list

def rand_data_extensor(data, len_extension):
    """Method for extending a sorted list (data) of random numbers by
    addding len_extension new ordered random_numbers at the end
    of the list.

    Parameters
    ----------
    data : [list] Sorted list to extend.
    len_extension : [int] Number of new elements to add to data.

    Returns
    -------
    data : [list] Sorted list with len_extension new elements at the end.
    """
    lower_bound = data[-1]
    for i in range(len_extension):
        rand_num = randint(lower_bound, lower_bound + 10)
        data.append(rand_num)
        lower_bound = rand_num + 1
    return data

def run_experiment(data, n):
    """Method for timing both methods over n runs by searching random numbers
    in data and taking the median over the n runs.
    """
    upper_bound = data[-1]
    veb_tree = StaticVEBTree(data)
    times = np.zeros((2, n))
    timer = Timer()
    
    # We search for n random numbers in data (100 times a number taking an average),
    # To finally return the median of all of them.
    for i in range(n):
        time_for_bs = 0
        time_for_veb = 0
        # We run the search for data[rand_index] 10 times and take the average
        rand_index = randint(0, len(data) - 1) 
        for j in range(100):
            timer.start()
            binary_search(data, data[rand_index])
            time_for_bs += timer.stop()
            timer.start()
            veb_tree.is_member(data[rand_index])
            time_for_veb += timer.stop()
        # We divide by 10 to take average and multiply by 1000 to convert to milliseconds. 
        times[0][i] = 1000 * (time_for_bs/100)  
        times[1][i] = 1000 * (time_for_veb/100)

    return [np.median(times[0]), np.median(times[1])]

def time_experiment(file_path_1, file_path_2):
    """Method for running experiments for lists of size i in {10^1, 10^2, 10^3, 10^4, 10^5, 10^6}
    and writting the resulting times in files file_path_1 for binary search and file_path_2 for
    StaticVEBTree is_member().
    """
    times_bs = []
    times_veb = []
    i = 10
    data = data_generator(i)

    while i <= int(1e6):
        temp_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[0]))
        print("Time for vEB-Tree search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[1]))
        times_bs.append(str(temp_times[0]))
        times_veb.append(str(temp_times[1]))
        len_extension = 10*i - i 
        data = rand_data_extensor(data, len_extension)
        i += len_extension
        
    with open(file_path_1, 'w') as f:
        f.write('\n'.join(times_bs))
 
    with open(file_path_2, 'w') as f:
        f.write('\n'.join(times_veb))

def time_data_generation_0(file_path_1, file_path_2):
    """Method for running experiments from arrays of size 10 to 1000 and writting the 
    resulting times in files file_path_1 for binary search and file_path_2 for
    StaticVEBTree is_member(). Takes increments of 1.
    """
    times_bs = []
    times_veb = []
    i = 10 
    data = data_generator(i)

    while i <= 1000:
        temp_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[0]))
        print("Time for vEB-Tree search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[1]))
        times_bs.append(str(temp_times[0]))
        times_veb.append(str(temp_times[1]))
        len_extension = 10
        data = rand_data_extensor(data, len_extension)
        i += len_extension
        
    with open(file_path_1, 'w') as f:
        f.write('\n'.join(times_bs))
 
    with open(file_path_2, 'w') as f:
        f.write('\n'.join(times_veb))

def time_data_generation_1(file_path_1, file_path_2):
    """Method for running experiments from arrays of size 1000 to 10000 and writting the 
    resulting times in files file_path_1 for binary search and file_path_2 for
    StaticVEBTree is_member(). Takes increments of 100.
    """
    times_bs = []
    times_veb = []
    i = 1000 
    data = data_generator(i)

    while i <= 10000:
        temp_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[0]))
        print("Time for vEB-Tree search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[1]))
        times_bs.append(str(temp_times[0]))
        times_veb.append(str(temp_times[1]))
        len_extension = 100
        data = rand_data_extensor(data, len_extension)
        i += len_extension
        
    with open(file_path_1, 'w') as f:
        f.write('\n'.join(times_bs))
 
    with open(file_path_2, 'w') as f:
        f.write('\n'.join(times_veb))

def time_data_generation_2(file_path_1, file_path_2):
    """Method for running experiments from arrays of size 1e4 to 1e5 and writting the 
    resulting times in files file_path_1 for binary search and file_path_2 for
    StaticVEBTree is_member(). Takes increments of 1000.
    """
    times_bs = []
    times_veb = []
    i = int(1e4)
    data = data_generator(i)

    while i <= int(1e5):
        temp_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[0]))
        print("Time for vEB-Tree search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[1]))
        times_bs.append(str(temp_times[0]))
        times_veb.append(str(temp_times[1]))
        len_extension = 1000
        data = rand_data_extensor(data, len_extension)
        i += len_extension
        
    with open(file_path_1, 'w') as f:
        f.write('\n'.join(times_bs))
 
    with open(file_path_2, 'w') as f:
        f.write('\n'.join(times_veb))

def time_data_generation_3(file_path_1, file_path_2):
    """Method for running experiments from arrays of size 1e5 to 1e6 and writting the 
    resulting times in files file_path_1 for binary search and file_path_2 for
    StaticVEBTree is_member(). Takes increments of 10000.
    """
    times_bs = []
    times_veb = []
    i = int(1e5)
    data = data_generator(i)

    while i <= int(1e6):
        temp_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[0]))
        print("Time for vEB-Tree search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[1]))
        times_bs.append(str(temp_times[0]))
        times_veb.append(str(temp_times[1]))
        len_extension = 10000
        data = rand_data_extensor(data, len_extension)
        i += len_extension
        
    with open(file_path_1, 'w') as f:
        f.write('\n'.join(times_bs))
 
    with open(file_path_2, 'w') as f:
        f.write('\n'.join(times_veb))
