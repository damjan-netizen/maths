# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 07:56:10 2021

@author: Network Damjan
"""
import ctypes
import numpy as np
from numpy import ctypeslib as npct

array_1d_double = npct.ndpointer(dtype=np.double,ndim=1,flags='CONTIGUOUS')

c_lib_numpy = npct.load_library('lib/sum', ".")
c_lib_numpy.sum.restype = ctypes.c_double
c_lib_numpy.sum.argtypes = [array_1d_double,ctypes.c_int]

c_lib_numpy.increment.restype = ctypes.c_int
c_lib_numpy.increment.argtypes = [ctypes.c_int]


a = np.arange(6)

epsilon = np.array([[8.5, 0.0, 0.0], 
                    [0.0, 8.5, 0.0], 
                    [0.0, 0.0, 8.5]])

n = c_lib_numpy.increment(9)
    
print(n)