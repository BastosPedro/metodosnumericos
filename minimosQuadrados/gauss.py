#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:41:52 2019

@author: pedro
"""

def gauss(A, B):
    """recebe as matrizes em forma de tuplas e resolve o sistema pelo metodo da eliminacao de gauss"""
    a = [list(x) for x in A]
    b = list(B)
    
    size = len (a)
    answer = [0] * size
    
    #primeira etapa do método, a eliminacao
    for k in range(size):
        if (abs(a[k][k]) < 1):
            auxmax = a[k][k]
            auxcount = k
            for m in range (k+1,size):
                if (abs(auxmax) < abs(a[m][k])):
                    auxcount = m
                    auxmax = a[m][k]
                    
            auxrow = a[k]
            a[k] = a[auxcount]
            a[auxcount] = auxrow
        
            bauxrow = b[k]
            b[k] = b[auxcount]
            b[auxcount] = bauxrow
              
    for j in range (size):
        for i in range (j+1,size):
            aux = a[i][j]/a[j][j]
            for k in range (size):
                a[i][k] = a[i][k] - aux*a[j][k]
            b[i] = b[i] - aux*b[j]
    #segunda etapa do método, a resolucao do sistema triangular
    answer[size-1] = b[size-1]/a[size-1][size-1]
    for k in range (size-1, -1, -1):
        s = 0
        for j in range (k+1, size):
            s = s + a[k][j] * answer[j]
        answer[k] = (b[k] - s)/a[k][k]
    
    return answer


