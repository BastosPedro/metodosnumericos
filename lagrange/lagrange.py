#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:31:57 2019

@author: pedro
"""

def lagrange (points, fpoints):
    """interpolacao pelo metodo de lagrange"""
    size = len(points)
    def p(x):
        p = 0
        for i in range (size):
            s = 1
            for j in range (size):
                if j != i:
                    s = (s * (x-points[j]))/(points[i]-points[j])
            p = p + fpoints[i]*s
        return p
    return p

pontos = [-1,0,2]
fpontos = [4,1,-1]



#print(teste(2))