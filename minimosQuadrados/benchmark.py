#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:48:47 2019

@author: pedro
"""

from minimos_quadrados import minimosQuadrados as minQuad
from scipy.optimize import curve_fit
from time import time
import numpy as np


def func(x, a, b, c, d, e):    
    """o scipy exige que seja dada uma funcao para a qual sera feito o ajuste"""    
    return a + b*x + (c*pow(x,2)) + (d*pow(x,3)) + (e*pow(x,4))

def benchmark(xvalues, yvalues):
    """dados os valores de x e seus respectivos valores f(x), a funcao faz o ajuste pelo metodo dos minimos quadrados feito a mao e pela solucao do scipy, retornando resultados e tempos"""
    
    startPy = time()
    funcPy = minQuad(xvalues, yvalues, 4)
    endPy = time()
    execPy = endPy - startPy
    
    
    startSciPy = time()
    funcScipy = curve_fit(func, xvalues,yvalues)
    endSciPy = time()
    execSciPy = endSciPy - startSciPy
    
    
    return funcPy, execPy, funcScipy, execSciPy


testeX = list(np.ravel(np.random.rand(1,5)))
testeY = list(np.ravel(np.random.rand(1,5)))

resultados = list()
[resultados.append(benchmark(testeX,testeY)) for x in range(3)]

mediaPy = sum(resultados[x][1] for x in range (3))/3
mediaScipy = sum(resultados[x][3] for x in range (3))/3
    
    
    