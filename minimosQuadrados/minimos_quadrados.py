#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:35:55 2019

@author: pedro
"""
from gauss import gauss

def minimosQuadrados (points, fpoints, power = 4):
    """essa funcao recebe os pontos, seus respectivos valores em f(x), e o grau do polinomio desejado"""
    
    n = int(power) + 1
    m = len(points)
    
    matrixA = [[0 for col in range(n)] for row in range(n)]    
    vectorB = [0] * n
    
    xks = [0] * ((2*power)+1)
    xks[0] = m
    
    
    for x in range (1, 2*power+1): #montando os valores que vao entrar na matriz A
        xks[x] = sum([pow(i,x) for i in points])
        
    print(xks)
        
    for x in range(n):
        for y in range(n): #colocando os valores achados na matriz A
            matrixA[x][y] = xks[x+y]
           
    for x in range (n): #montando o vetor B
        vectorB[x] = sum([pow(points[j],x)*fpoints[j] for j in range(m)]) 
        
    #print(matrixA)
    #print(vectorB)

    
    auxA = tuple([tuple(x) for x in matrixA])
    auxB = tuple(vectorB)
    
    coefs = gauss(auxA, auxB)
    
    print(coefs)
    
    def func(x):
        func = 0
        for count in range(power):
            func = func + coefs[count] * pow(x,count)
        return func
    
    return func, coefs


    
    
testeX = [0, 0.25, 0.5, 0.75, 1]
testeFx = [1, 1.284, 1.6487, 2.117, 2.7813]

resposta = minimosQuadrados (testeX, testeFx, 4)    
    
        
    