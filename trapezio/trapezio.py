#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:19:42 2019

@author: pedro
"""

def trapezio (a, b, n, func):
    h = (b-a)/n
    Sum = 0
    for count in range (1,n):
        aux = a + h*(count-1)
        Sum = Sum + func(aux)
    return (h/2)*((2*Sum) + func(a) + func(b))
