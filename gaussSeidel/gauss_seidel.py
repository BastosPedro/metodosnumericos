#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:35:02 2019

@author: pedro
"""
import numpy as np

def gauss_seidel (a, b, tol, nitemax, x0):
    nite = 0
    dist = 0
    size = len(a)
    x = x0
    s = np.zeros(2)
    while dist < tol and nite < nitemax:
        nite = nite+1
        for i in range (size):
            s[0] = b[i]
            s[1] = 0
            for j in range (i):
                s[0] = s[0] - a[i][j] * x[j]
            for j in range (i+1, size):
                s[1] = s[1] - a[i][j] * x0[j]  
            x[i] = (s[0]+s[1])/a[i][i]
        aux = [x[i]-x0[i] for i in range(len(a))]
        dist = pow(sum(x**2 for x in aux),0.5)
        x0 = x
    return x0
            
