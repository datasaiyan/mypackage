# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 23:20:01 2019

@author: shin
"""
def sum_array(array):

    if len(array) == 0:
        return(0)
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    if n == 0:
        return(0)
    elif n == 1 | n == 2:
        return(1)
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

def factorial(n):
    if n == 0 | n == 1:
        return(1)
    else:
        return(n * factorial(n - 1))

def reverse(word):
    if word == "":
        return(word)
    else:
        word[-1] + reverse(word[:-1])
