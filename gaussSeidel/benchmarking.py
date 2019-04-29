#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:08:53 2019

@author: pedro
"""

from time import time
import numpy as np
import gauss_seidel

def getMatrix (size = 20):
    """gera uma matriz que sempre vai convergir conforme o criterio das linhas"""
    matrix = np.random.rand(size,size)
    for x in range(size):
        matrix[x][x] = sum(map(abs,matrix[x]))
    return matrix


def benchmark(testeA, testeB):
    """dadas as matrizes A e B, é comparada o tempo de execução por Gauss-Seidel e NumPy"""
    
    startNumPy = time()
    respostaNumPy = np.linalg.solve(testeA,testeB)
    endNumPy = time()

    execNumPy = endNumPy - startNumPy
    del endNumPy, startNumPy

    chute = np.zeros(len(testeB))
    startGauss = time()
    respostaGauss = gauss_seidel.gauss_seidel(testeA,testeB, 0.1, 10, chute)
    endGauss = time()
    
    execGauss = endGauss - startGauss
    del endGauss, startGauss, chute
    
    return respostaNumPy, execNumPy, respostaGauss, execGauss



    
matrizA = getMatrix(20)
matrizB = np.random.rand(20,1)

teste = list()
[teste.append(benchmark(matrizA,matrizB)) for x in range (3)]

mediaNumPy = sum(teste[x][1] for x in range (3))/3
mediaGauss = sum(teste[x][3] for x in range (3))/3

