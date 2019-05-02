#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:09:24 2019

@author: pedro
"""

from lagrange import lagrange as pyLagrange
from quadrilateral_quadratico import quadrilateralQuadratico as quadLat
from scipy.interpolate import lagrange as spLagrange
from time import time
import numpy as np



def getValues(npoints, nfunctions):
    """cria os valores a serem usados para a interpolação randomicamente"""
    values = list()
    for x in range (nfunctions):
        values.append([np.ravel(np.random.rand(1,npoints)), np.ravel(np.random.rand(1,npoints))])
    return values


def lagrangeList(values):
    """interpola os valores dados, usando o metodo de lagrange feito a mao, retornado uma lista de funcoes"""
    size = len(values)
    funcList = list()
    
    for x in range(size):
        funcList.append(pyLagrange(values[x][0],values[x][1]))
    
    return funcList

def SciPyList(values):
    """interpola os valores dados, usando o metodo de lagrange do SciPy, retornado uma lista de funcoes"""
    size = len(values)
    funcList = list()
    
    for x in range(size):
        funcList.append(spLagrange(values[x][0],values[x][1]))
    
    return funcList
   
def benchmark (valores):
    "testando os dois metodos, passando como argumentos os valores de x e y e retornando as matrizes com as funcoes e o tempo de execucao com scipy e lagrange no braço"
        
    startSp = time()
    funcSp = SciPyList(valores)
    matrixSp = quadLat(funcSp)
    endSp = time()
    execSp = endSp - startSp
    
    startPy = time()
    funcPy = lagrangeList(valores)
    matrixPy = quadLat(funcPy)
    endPy = time()
    execPy = endPy - startPy
    
    
    return matrixPy, execPy, matrixSp, execSp



teste = getValues(3,3)

resultados = list()
[resultados.append(benchmark(teste)) for x in range(3)]

mediaPy = sum(resultados[x][1] for x in range (3))/3
mediaScipy = sum(resultados[x][3] for x in range (3))/3

