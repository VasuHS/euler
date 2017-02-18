# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 20:12:46 2016

@author: Vasu
"""
import timeit
    
def fib_gen():
    first=1
    yield first
    second=2
    yield second
    #i=3
    while(True):
        third=first+second
        if third < 4000000:
            yield third
        else:
            break
        first=second
        second=third
 
def fib_sum(): 
    sum1=0
    for i in fib_gen():
        if i & 1 ==0:
            sum1=sum1+i
    return sum1

print fib_sum()       
print timeit.timeit(fib_sum)
