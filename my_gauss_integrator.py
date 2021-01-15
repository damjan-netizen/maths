# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:00:52 2021

@author: Network Damjan
"""

import numpy as np
from numpy.linalg import inv
from time import time

def measure_time(function):
    def timed(*args, **kwargs):
        begin = time()
        result = function(*args, *kwargs)
        end = time()
        
        print('Completed in {:f} seconds.'.format(end-begin))
        return result
    return timed

# def measure_time(function):
#     def timed(*args, **kwargs):
#         begin = time()
#         result = function(*args, **kwargs)
#         end = time()
 
#         print('Completed in {:5.3f} seconds'.format(end - begin))
#         return result
#     return timed

N = 100
G_max = 20
sigma = 0.7
epsilon = np.array([[8.5, 0.0, 0.0],
                    [0.0, 8.5, 0.0],
                    [0.0, 0.0, 8.5]])

kx_vector = np.linspace(-G_max, G_max, N, endpoint=False)
ky_vector = np.linspace(-G_max, G_max, N ,endpoint=False)
kz_vector = np.linspace(-G_max, G_max, N, endpoint=False)

def function(k, epsilon, sigma, G_max):
    k_mod = np.dot(k,k)
    if k_mod<G_max**2:
        kek = np.dot(k,np.dot(epsilon,k))
        return np.exp(-sigma**2*kek)/kek
    return 0.0
    
@measure_time
def integrate():
    integral = 0
    for kx in kx_vector:
        for ky in ky_vector:
            for kz in kz_vector:
                if(kx==0 and ky==0 and kz==0):
                    pass
                else:
                    k = np.array([kx,ky,kz])
                    value = function(k,epsilon,sigma,G_max)
                    integral += value
    volume_element = (2*G_max/N)**3
    return integral*volume_element/2/np.pi**2
    
value = integrate()

print('Final value after {:d} iterations is {:4.4f}'.format(N,value))