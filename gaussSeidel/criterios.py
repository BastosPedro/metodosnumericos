#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:55:24 2019

@author: pedro
"""

def crit_linha (a):
    size = len(a)
    rowalpha = [0] * size
    for i in range(size):
        rowalpha[i] = (sum(map(abs, a[i])) - abs(a[i][i]))/abs(a[i][i])
    return max(rowalpha)

def crit_coluna (a):
    size = len(a)
    columnalpha = [0] * size
    for x in range(size):
        for y in range(size):
            columnalpha[x] = columnalpha[x] + abs(a[y][x])
        columnalpha[x] = (columnalpha[x] - abs(a[x][x]))/abs(a[x][x])
    print (columnalpha)
    return max(columnalpha)
    
def crit_sass(a):
    size = len(a)
    sassalpha = [0] * size
    for x in range (1,size):
        sassalpha[0] = sassalpha[0] + abs(a[0][x])
    
    sassalpha[0] = sassalpha[0]/abs(a[0][0])
    
    for x in range (1, size):
        for y in range(size):
            if (y <= x-1):
                sassalpha[x] = sassalpha[x] + abs(a[x][y]) * sassalpha[y]
            else:
                sassalpha[x] = sassalpha[x] + abs(a[x][y])
        sassalpha[x] = (sassalpha[x] - abs(a[x][x]))/abs(a[x][x])
    
    return max(sassalpha)


teste = [[10,2,1],[1,5,1],[2,3,10]]

print(crit_linha(teste))
print(crit_coluna(teste))
print(crit_sass(teste))
        