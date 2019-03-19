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

def fibonacci(number):
    """
    the Fibonacci sequenceis characterized by the fact that every number
    after the first two is the sum of the two preceding ones
    """
    if number == 1:
        return 1
    elif number <= 0:
        return(0)
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

def factorial(n):
    if n == 0 | n == 1:
        return(1)
    else:
        return(n * factorial(n - 1))

def reverse(word):
    if word == "":
        return(word)
    else:
        return(word[-1] + reverse(word[:-1]))
