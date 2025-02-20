#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:45:48 2025

@author: thynguyen
"""

import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish)  
    result = np.full(numbers.shape, '', dtype=object) 
    
    result[numbers % 3 == 0] = 'Fizz'
    result[numbers % 5 == 0] = 'Buzz'
    result[numbers % 15 == 0] = 'FizzBuzz'

    mask = result == ''
    result[mask] = numbers[mask].astype(str)

    return result

start = 91
finish = 106  
print("\n".join(FizzBuzz(start, finish)))

myEmptyList = []
for i in range(91, 105):
    myEmptyList.append(i)
    
print(myEmptyList)  