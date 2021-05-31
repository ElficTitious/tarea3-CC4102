import numpy as np
from utilities.math_functions import *
from algorithms.static_veb_node import StaticVEBNode


class StaticVEBTree:
    """Wrapper class for StaticVEBNode.
    """

    def __init__(self, data):
        """Initializes self.u to the next power of two after the last element in data
        (because we need the universe size to be an exact power of two). And instantiates the
        self.root of the tree to be a StaticVEBNode with universe size u  and the given data.

        Parameters
        ----------
        data : [list] Sequence of integers to be stored in the vEB node root.
        """
        self.u = next_power_of_two(data[-1]) if not is_power_of_two(data[-1]) \
                 else 2 * next_power_of_two(data[-1])
        bit_map = self.__data_to_bit_map(data)
        self.root = StaticVEBNode(bit_map, self.u)

    def is_member(self, x):
        """Method that provides a wrapper to the StaticVEBNode.is_member() method.

        Parameters
        ----------
        x : [int] Number which to assert membership in the tree.

        Returns
        -------
        True if x belongs to the tree and False otherwise.
        """ 
        return self.root.is_member(x)

    def __data_to_bit_map(self, data):
        """Method used to convert the data into a bit map.
        Used to initialize the root (StaticVEBNode) whose constructor needs a bit map.
        """
        bit_map = np.zeros(self.u)
        ptr_data = 0
        ptr_bit_map = 0
        for num in data:
            bit_map[num] = 1

        return bit_map

if __name__ == "__main__":
    
    even_num_arr = np.array([i for i in range(1000) if i % 2 == 0])
    static_veb_tree = StaticVEBTree(even_num_arr)
    for i in range(1000):
        if i % 2 == 0:
            assert(static_veb_tree.is_member(i))
        else:
            assert(not static_veb_tree.is_member(i))
