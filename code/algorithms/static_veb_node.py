import numpy as np
from utilities.math_functions import *
from math import *

class StaticVEBNode:
    """Class that represents a node of a static version of the structure vEB tree.
    """

    def __init__(self, bin_map, u):
        """Recursively initializes a StaticVEBNode.  
    
        Parameters
        ----------
        bin_map : [numpy.ndarray] Binary map of the information to be
                  stored in the node.
        u : [int] Universe size for the node.
        """
        self.bin_map = bin_map
        self.u = u
        if not self.__is_empty():
            self.__init_max()
            self.__init_min()

        else:  # If there is no data to be stored in the node, both fields are null.
            self.min = None
            self.max = None
        self.__initialize_children()  # We need to recursively initialize all the children nodes.
    
    def __is_empty(self):
        for i in range(self.u):
            if self.bin_map[i] == 1:
                return False
        return True

    def __init_min(self):
        self.min = np.argmax(self.bin_map)
        self.bin_map[self.min] = 0

    def __init_max(self):
        reverse_bin_map = self.bin_map[::-1]
        self.max = len(reverse_bin_map) - np.argmax(reverse_bin_map) - 1


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

    def __partition_bin_maps(self):
        partitioned_bin_maps = np.zeros((upper_sqrt(self.u), lower_sqrt(self.u)))
        i = 0
        ptr_bin_maps = 0
        while i < self.u:
            while self.__high(i) == ptr_bin_maps:
                if self.bin_map[i] == 1:
                    partitioned_bin_maps[ptr_bin_maps][self.__low(i)] = 1
                i += 1
            ptr_bin_maps += 1

        return partitioned_bin_maps 

    def __initialize_children(self):
        """Method used in the constructor of this class for initializing the children 
        of the current node.
        """ 
        if self.u == 2:  # If the current node is of base size, the cluster is null; that is, it doesn't have any children.
            self.cluster = None
        else:
            self.cluster = []
            partitioned_bin_maps = self.__partition_bin_maps()
            for i in range(upper_sqrt(self.u)):
                temp_node = StaticVEBNode(partitioned_bin_maps[i], lower_sqrt(self.u))
                self.cluster.append(temp_node)

        self.cluster = np.array(self.cluster)

    
    def is_member(self, x):
        if (self.min is not None and self.max is not None) and (x == self.min or x == self.max):
            return True
        elif self.u == 2 : return False
        # Else we search the number given by the least significant floor(log2(u)/2) bits of x in the cluster with index __high(x).
        else:  
            return self.cluster[self.__high(x)].is_member(self.__low(x))
