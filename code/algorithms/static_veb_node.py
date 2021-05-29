import numpy as np
from utilities.math_functions import *
from math import *

class StaticVEBNode:
    """Class that represents a node of a static version of the structure vEB tree.
    """

    def __init__(self, data, u):
        """Recursively initializes a StaticVEBNode.  
    
        Parameters
        ----------
        data : [int] Numbers to be stored in the node.
        u : [int] Universe size for the node.
        """
        self.u = u
        self.cluster = []
        if len(data) > 0:
            data = list(dict.fromkeys(data))  # Because this structure is recursive we need
                                              # to erase duplicates.
            self.min = data[0]
            self.max = data[-1]
            data.pop(0)  # We remove the minimum.
        else:  # If there is no data to be stored in the node, both fields are null.
            self.min = None
            self.max = None
        self.initialize_children(data)  # We need to recursively initialize all the children nodes.

    def high(self, x):
        """Method for calculating the most significant ceil(log2(u)/2) bits of x.

        Parameters
        ----------
        x : [int] Number for which to calculate the most significant ceil(log2(u)/2) bits.

        Returns
        -------
        result : [int] floor(x / lower_sqrt(self.u)), the 
                 most significant ceil(log2(u)/2) bits of x.
        """
        result = floor(x / lower_sqrt(self.u))
        return result
    
    def low(self, x):
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

    def partition_data(self, data):
        """Method for partitioning the data of the node so that the method initializeChildren()
        can construct each children with it's own share of the data to be stored.
    
        Parameters
        ---------
        data : [list] List of ints to be partitioned.

        Returns
        -------
        partition : [list] Partitioned data of size upperSqrt(self.u) to
                    initialize the children of the current node.
        """
        partition = []
        i = j = 0
        while i < upper_sqrt(self.u):
            temp = []
            while (j < len(data) and self.high(data[j]) == i):
                temp.append(data[j])
                j += 1
            partition.append(temp)
            i += 1
        return partition

    def initialize_children(self, data):
        """Method used in the constructor of this class for initializing the children 
        of the current node.

        Parameters
        ----------
        data : [list] Data being stored in the node.
        """ 
        if self.u == 2:  # If the current node is of base size, the cluster is null; that is, it doesn't have any children.
            self.cluster = None
        else:
            partitioned_data = self.partition_data(data)  # We partition the data to give each children its corresponding share.
            for i in range(upper_sqrt(self.u)):
                # We apply the map low() to each element and sort the resulting list to keep the invariant.
                low_temp_data = sorted([self.low(e) for e in partitioned_data[i]])
                temp_node = StaticVEBNode(low_temp_data, lower_sqrt(self.u))
                self.cluster.append(temp_node)

    
    def is_member(self, x):
        if (self.min is not None and self.max is not None) and (x == self.min or x == self.max):
            return True
        elif self.u == 2 : return False
        # Else we search the number given by the least significant floor(log2(u)/2) bits of x in the cluster with index high(x).
        else:  
            return self.cluster[self.high(x)].is_member(self.low(x))
