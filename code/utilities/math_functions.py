from math import *

def next_power_of_two(x):
    result = 1 << ceil(log2(x))
    return result

def prev_power_of_ten(x):
    result = 10 ** floor(log10(x))
    return result

def lower_sqrt(x):
    result = 1 << floor(log2(x)/2)
    return result
 

def upper_sqrt(x):
    result = 1 << ceil(log2(x)/2)
    return result
 

if __name__ == "__main__":
     print(prev_power_of_ten(3))