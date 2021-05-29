
import numpy as np
from timeit import timeit
from algorithms.binary_search import binary_search
from algorithms.static_veb_tree import StaticVEBTree
from utilities.math_functions import *
from random import *

def data_generator(N):
    lower_bound = 0
    temp_list = []
    for i in range(N):
        rand_num = randint(lower_bound, lower_bound + 10)
        temp_list.append(rand_num)
        lower_bound = rand_num + 1
    return temp_list

def rand_data_extensor(data, len_extension):
    lower_bound = data[-1]
    for i in range(len_extension):
        rand_num = randint(lower_bound, lower_bound + 10)
        data.append(rand_num)
        lower_bound = rand_num + 1
    return data

def run_experiment(data, n):
    upper_bound = data[-1]
    veb_tree = StaticVEBTree(data)
    times = np.zeros((2, n))
    
    for i in range(n):
        rand_num = randint(0, upper_bound)
        time_for_bs = timeit('binary_search(data, rand_num)',
                                  number=1, globals={'binary_search':globals().get('binary_search'), 'data':locals().get('data')
                                                     ,'rand_num':locals().get('rand_num')})
        time_for_veb = timeit('veb_tree.is_member(rand_num)', number=1, globals=locals())
        times[0][i] = 1000 * time_for_bs
        times[1][i] = 1000 * time_for_veb

    return [np.median(times[0]), np.median(times[1])]

def time_data_generation(n, file_path_1, file_path_2):
    times_bs = []
    times_veb = []
    i = 2
    data = data_generator(i)

    while i <= n:
        temp_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[0]))
        print("Time for vEB-Tree search for array of size {} is {:.5f} milliseconds.".format(i, temp_times[1]))
        times_bs.append(str(temp_times[0]))
        times_veb.append(str(temp_times[1]))
        len_extension = prev_power_of_ten(i)
        data = rand_data_extensor(data, len_extension)
        i += len_extension
        
    with open(file_path_1, 'w') as f:
        f.write('\n'.join(times_bs))
 
    with open(file_path_2, 'w') as f:
        f.write('\n'.join(times_veb))


if __name__ == "__main__":

    
    n = 10
    while n <= int(1e6):
        data = data_generator(n)
        rand_num = randint(0, n)
        median_times = run_experiment(data, 4)
        print("Time for binary search for array of size {} is {} milliseconds.".format(n, median_times[0]))
        print("Time for vEB-Tree search for array of size {} is {} milliseconds.".format(n, median_times[1]))
        n *= 10
        """
        if n < int(1e4) : n += 100
        elif n < int(1e5) : n += 1000
        else : n += prev_power_of_ten(n)/10
        """
