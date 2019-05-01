#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:32:07 2019

Thanks users "Hunter" and "Alex Hall" on StackOverflow!

@author: pedro 

"""
def partialDifferenceQuotient (f, v, i, h):
    "retorna a derivada parcial no ponto"
    w = [vj + (h if j==i else 0) for j, vj in enumerate(v)]
    
    return (f(w) - f(v))/h

def estimateGradient(f, v, h = 1e-10):
    "usando a outra funcao, estima oa gradiente"
    return [partialDifferenceQuotient(f,v,i,h) for i, _ in enumerate(v)]


def jacobian (functions, variables):
    "monta a jacobiana"
    j = list()
    size = len(functions)
    [j.append(estimateGradient(functions[x], variables)) for x in range (size)]
    return j

"""
so vendo se pegava
def f(v):
    x, y, z = v
    return (x*x) + (x*y*y) + z

teste = [f,f]

resposta = jacobian(teste, [3,3,4])

"""