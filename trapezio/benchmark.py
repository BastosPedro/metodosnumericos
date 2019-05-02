#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:49:52 2019

@author: pedro
"""

from trapezio import trapezio
from scipy.integrate import quad
from numpy.random import randint
from time import time

def teste (x):
    return pow(x,6)

def IntTest (a,b):
    return (pow(b,7)/7) - (pow(a,7)/7)

def trapezioConvergente (a, b, tol = 0.001, func = teste, intFunc = IntTest):
    count = 10
    while (intFunc(a,b) - trapezio(a,b, count, func)) > tol and count < 1000:
        count +=1
    return trapezio(a,b,count,func), count

def benchmark (a, b, tol = 0.001, func = teste, intFunc = IntTest):
    
    startPy = time()
    intPy = trapezioConvergente (a,b)
    endPy = time()
    execPy = endPy - startPy
    
    startSciPy = time()
    intSciPy = quad(func,a,b)
    endSciPy = time()
    execSciPy = endSciPy - startSciPy
    
    return intPy, execPy, intSciPy, execSciPy

intervalA = randint(10)
intervalB = randint(10, 100)
resultados = list()
[resultados.append(benchmark(intervalA,intervalB)) for x in range(3)]

mediaPy = sum(resultados[x][1] for x in range (3))/3
mediaScipy = sum(resultados[x][3] for x in range (3))/3
    
    