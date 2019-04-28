#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:08:53 2019

@author: pedro
"""

from time import time
import numpy as np
import criterios
import gauss_seidel

def getSafeValues (size = 20, limit = 1000):
    print (size)
    count = 0
    while count < limit:
        count = count + 1
        candidate = np.random.rand(size,size)
        
        if (criterios.crit_coluna(candidate)) < 1:
            break
        elif  (criterios.crit_linha(candidate)) < 1:
            break
        elif (criterios.crit_sass(candidate)) < 1:
            break
        
    if count < limit:
        print("convergiu! total de tentativas: ", count)
    else:
        print("sem garantias...")
    return candidate


"""teste com valores variáveis"""
def variableBenchmark (size = 20, limit = 1000):
    testeA = getSafeValues(size, limit)
    testeB = np.random.rand(size,1)

    startNumPy = time()
    respostaNumPy = np.linalg.solve(testeA,testeB)
    endNumPy = time()

    execNumPy = endNumPy - startNumPy
    del endNumPy, startNumPy


    chute = np.zeros(size)
    startGauss = time()
    respostaGauss = gauss_seidel.gauss_seidel(testeA,testeB, 0.1, 10, chute)
    endGauss = time()

    execGauss = endGauss - startGauss
    del endGauss, startGauss, chute
    
    return respostaNumPy, execNumPy, respostaGauss, execGauss, testeA, testeB


"""teste com valores fixos"""
def fixedBenchmark():
    
    testeA = [[3,1,1],[1,4,2],[0,2,5]]
    testeB = np.array([7,4,5])
    
    startNumPy = time()
    respostaNumPy = np.linalg.solve(testeA,testeB)
    endNumPy = time()

    execNumPy = endNumPy - startNumPy
    del endNumPy, startNumPy

    chute = np.zeros(3)
    startGauss = time()
    respostaGauss = gauss_seidel.gauss_seidel(testeA,testeB, 0.1, 10, chute)
    endGauss = time()
    
    execGauss = endGauss - startGauss
    del endGauss, startGauss, chute
    
    return respostaNumPy, execNumPy, respostaGauss, execGauss


teste1 = variableBenchmark(20, 40000)
print("diferenca de tempo no teste variavel foi de:", teste1[3]-teste1[1])
#teste2 = fixedBenchmark()
#print("diferenca de tempo no texte 3x3 fixo foi de:", teste2[3]-teste2[1])

#testealpha = np.random.rand(4,4)