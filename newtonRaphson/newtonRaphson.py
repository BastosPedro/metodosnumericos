#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:10:01 2019

@author: pedro
"""

from gauss import gauss
from jacobiana import jacobian
from support import evaluate, norm, sumMatrices


def newtonRaphson(funcMatrix, x0, epsilon=0.0001, niteMax=10):
    """o metodo de newton raphson"""
    xk = [0] * (niteMax+1)
    xk[0] = x0
    
    for k in range(niteMax):
        if norm(evaluate(funcMatrix, xk[k])) < epsilon:
            break
        else:
            fxk = [i*-1 for  i in evaluate(funcMatrix,xk[k])]
            jxk = jacobian(funcMatrix, xk[k])
            dx = gauss(jxk, fxk)
            xk[k+1] = sumMatrices(xk[k], dx)
    
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


