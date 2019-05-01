#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:38:35 2019

@author: pedro
"""
from math import sqrt

def evaluate(funcMatrix, values):
    """pega um vetor de funcoes, os valores, e executa cada funcao nos valores"""
    size = len(funcMatrix)
    answer = [0] * size
    for x in range(size):
        answer[x]  = funcMatrix[x](values)
    return answer
    
def norm(x):
    """norma do vetor"""
    return sqrt(sum(pow(i,2) for i in x))

def sumMatrices(a,b):
    """soma matrizes 1xN ou Nx1"""
    size = len(a)
    result = [0]*size
    for i in range (size):
        result[i] = a[i] + b[i]
    return result