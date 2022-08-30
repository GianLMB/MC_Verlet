# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:46:03 2020

@author: giang
"""

# Lecture 3.3 Probability & Information
# random generator with p = 0.4

import numpy as np
import matplotlib.pyplot as plt
import random as rnd

rnd.seed()
n_rep = int(1e3)
p = rnd.random()   # 0.4
n = np.arange(n_rep+1)
k = np.zeros(n_rep+1)

for i in range(1,n_rep+1):
    w = rnd.random()
    if w < p: k[i] = k[i-1]+1
    else: k[i] = k[i-1]
    
plt.plot(n[1:],k[1:]/n[1:])


#%%

# unknown probability

a = 1.0
k = np.zeros(n_rep+1)

for i in range(1,n_rep+1):
    w = rnd.random()
    if w*(n[i-1]+3*a) < (k[i-1]+a): k[i] = k[i-1]+1
    else: k[i] = k[i-1]
    
plt.plot(n[1:],k[1:]/n[1:])