#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:28:33 2019

@author: pedro
"""

def produtoDeFuncao (f,g):
    """pega uma funcao f(x) e g(y) e obtem fg(x,y) = f(x)*g(y)"""
    def fg(x,y):
        return f(x)*g(y)
    return fg

def quadrilateralQuadratico (funcList):
    """elabora a matriz quadrilateral quadratica"""
    size = len(funcList)
    functions = [[0 for col in range(size)] for row in range(size)]
    for x in range (size):
        for y in range(size):
            functions[x][y] = produtoDeFuncao(funcList[x],funcList[y])
    return functions