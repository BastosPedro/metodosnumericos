#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:49:52 2019

@author: pedro
"""

from trapezio import trapezio
from scipy.integrate import quad
from time import time

def teste (x):
    return pow(x,2)

def IntTest (a,b):
    return (pow(b,3)/3) - (pow(a,3)/3)

def trapezioConvergente (a, b, tol = 0.001, func = teste, intFunc = IntTest):
    count = 10
    while (intFunc(a,b) - trapezio(a,b, count, func)) > tol:
        count +=1
    return trapezio(a,b,count,func), count

#resultado = trapezioConvergente (0,2)

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

resultados = list()
[resultados.append(benchmark(0,2)) for x in range(3)]

mediaPy = sum(resultados[x][1] for x in range (3))/3
mediaScipy = sum(resultados[x][3] for x in range (3))/3
    
    