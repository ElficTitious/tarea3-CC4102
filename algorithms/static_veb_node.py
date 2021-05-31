import numpy as np
from utilities.math_functions import *
from math import *

class StaticVEBNode:
    """Class that represents a node of a static version of the structure vEB tree.
    """

    def __init__(self, bit_map, u):
        """Recursively initializes a StaticVEBNode.  
    
        Parameters
        ----------
        bit_map : [numpy.ndarray] Bit map of the information to be
                  stored in the node.
        u : [int] Universe size for the node.
        """
        self.u = u
        if not self.__is_empty(bit_map):
            self.__init_max(bit_map)
            self.__init_min(bit_map)
            bit_map[self.min] = 0  # Because we do not store min in the children, we erase it from the bit map

        else:  # If there is no data to be stored in the node, both fields are null.
            self.min = None
            self.max = None
        self.__initialize_children(bit_map)  # We need to recursively initialize all the children nodes.
    
    def __is_empty(self, bit_map):
        """Returns False if there is no elements stored in the bit map and True otherwise. 
        """
        for i in range(self.u):
            if bit_map[i] == 1:
                return False
        return True

    def __init_min(self, bit_map):
        """Initializes the min field.
        """
        self.min = np.argmax(bit_map)

    def __init_max(self, bit_map):
        """Initializes the max field.
        """
        reverse_bit_map = bit_map[::-1]
        self.max = len(reverse_bit_map) - np.argmax(reverse_bit_map) - 1


    def __high(self, x):
        """Method for calculating the most significant ceil(log2(u)/2) bits of x.

        Parameters
        ----------
        x : [int] Number for which to calculate the most significant ceil(log2(u)/2) bits.

        Returns
        -------
        result : [int] floor(x / __lower_sqrt(self.u)), the 
                 most significant ceil(log2(u)/2) bits of x.
        """
        result = floor(x / lower_sqrt(self.u))
        return result
    
    def __low(self, x):
        """Method for calculating the most least sifnificant floor(log2(u)/2) bits of x.

        Parameters
        ----------
        x : [int] Number for which to calculate the most significant floor(log2(u)/2) bits.

        Returns
        -------
        result : [int] x % lower_sqrt(self.u)), the least significant  ceil(log2(u)/2) bits
                 of x.
        """
        result = x % lower_sqrt(self.u)
        return result

    def __partition_bit_maps(self, bit_map):
        """Method used for partitioning the bit map in order to recursively store the elements
        in the children.
        """
        partitioned_bit_maps = np.zeros((upper_sqrt(self.u), lower_sqrt(self.u)))
        i = 0
        ptr_bit_maps = 0
        while i < self.u:
            while self.__high(i) == ptr_bit_maps:
                if bit_map[i] == 1:
                    partitioned_bit_maps[ptr_bit_maps][self.__low(i)] = 1
                i += 1
            ptr_bit_maps += 1

        return partitioned_bit_maps 

    def __initialize_children(self, bit_map):
        """Method used in the constructor of this class for initializing the children 
        of the current node.
        """  
        # If the current node is of base size, the cluster is null; that is, it doesn't have any children.
        if self.u == 2: 
            self.cluster = None
        else:
            self.cluster = []
            partitioned_bit_maps = self.__partition_bit_maps(bit_map)
            for i in range(upper_sqrt(self.u)):
                temp_node = StaticVEBNode(partitioned_bit_maps[i], lower_sqrt(self.u))
                self.cluster.append(temp_node)

        self.cluster = np.array(self.cluster)

    
    def is_member(self, x):
        """Recursive Method used for asserting membership in the node. Returns True if the number x is 
        stored in this node and False otherwise.

        Paramaters
        ----------
        x : [int] Element to assert membership in the node.

        Returns
        -------
        [bool] True if x is stored in the node and False otherwise.
        """
        if (self.min is not None and self.max is not None) and (x == self.min or x == self.max):
            return True
        elif self.u == 2 : return False
        # Else we search the number given by the least significant floor(log2(u)/2) bits of x in the cluster with index __high(x).
        else:  
            return self.cluster[self.__high(x)].is_member(self.__low(x))
