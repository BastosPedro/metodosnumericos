#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:10:01 2019

@author: pedro
"""

from gauss import gauss
from jacobiana import jacobian
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

def newtonRaphson(funcMatrix, x0, epsilon=0.0001, niteMax=10):
    """o metodo de newton raphson"""
    xk = [0] * (niteMax+1)
    xk[0] = x0
    
    for k in range(niteMax):
        if norm(evaluate(funcMatrix, xk[k])) < epsilon:
            break
        else:
            fxk = [i*-1 for  i in evaluate(funcMatrix,xk[k])]
            print(fxk)
            jxk = jacobian(funcMatrix, xk[k])
            print(jxk)
            dx = gauss(jxk, fxk)
            print(dx)
            xk[k+1] = sumMatrices(xk[k], dx)
            print(xk)
    
    print(xk)
    return xk[k]
    
def f1(v):
    """metodo para teste"""
    x1, x2 = v
    return x1+x2-3

def f2(v):
    """metodo para teste"""
    x1, x2 = v
    return pow(x1,2) + pow(x2,2) - 9

chute = [1,5]

funcoes = [f1,f2]

resposta = newtonRaphson(funcoes, chute)


