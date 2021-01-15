# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:01:35 2021

@author: Network Damjan
"""

import ctypes
from time import time
import numpy as np
from numpy import ctypeslib as npct

cpp_lib = npct.load_library('C++/lib/integrator', ".")
c_array1D_double = npct.ndpointer(dtype=np.double,ndim=1,flags='CONTIGUOUS')

cpp_lib.function.restype = ctypes.c_double
cpp_lib.function.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                             c_array1D_double,ctypes.c_double, ctypes.c_double]
cpp_lib.integrate.restype =ctypes.c_double
cpp_lib.integrate.argtypes = [ctypes.c_int, ctypes.c_double, c_array1D_double,
                              ctypes.c_double]

sigma = 0.7
epsilon = np.array([[8.5, 0.0, 0.0],
                    [0.0, 8.5, 0.0],
                    [0.0, 0.0, 8.5]])

G_max = 20
N=100
