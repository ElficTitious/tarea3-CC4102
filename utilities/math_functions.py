from math import *

def next_power_of_two(x):
    """Returns the next power of two after x.
    """
    result = 1 << ceil(log2(x))
    return result

def is_power_of_two(x):
    """Returns if x is a power of two or not.
    """
    return log2(x).is_integer()

def prev_power_of_ten(x):
    """Returns the previous power of ten before x.
    """
    result = 10 ** floor(log10(x))
    return result

def lower_sqrt(x):
    """Returns the lower square root of x, defined as
    2^(floor(log2(x)/2)).
    """
    result = 1 << floor(log2(x)/2)
    return result
 

def upper_sqrt(x):
    """Returns the upper square root of x, defined as
    2^(ceil(log2(x)/2)).
    """
    result = 1 << ceil(log2(x)/2)
    return result
 

if __name__ == "__main__":
     print(prev_power_of_ten(3))
     print(is_power_of_two(8))
     print(is_power_of_two(21))
