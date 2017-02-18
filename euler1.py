# -*- coding: utf-8 -*-
"""
Created on Tue Mar 01 20:52:54 2016

@author: Vasu
"""
"""
4 diffenrt ways of solving a problem of finding the sum of numbers bettween 1-1000
which are divide by 3 or 5
1)normal method which has the call
2) list comperhensive wiht sum buitin function use
3)use of generator way of calling the result from sum methd
4)using the 
"""
import time
import timeit

def timeme(method):
    def funarg(*arg,**argv):
        start=time.clock()
        method(*arg,**argv)
        end=time.clock()
        print (end-start)
    return funarg

@timeme
def Mul30r5():
    sum1=0    
    l=[x for x in range(3,1000) if x%3==0 or x%5==0]
    for i in l:
        sum1=sum1+i
    return sum1


print Mul30r5()



print timeit.timeit("sum([x for x in range(3,1000) if x%3==0 or x%5==0])",number=1)

print (sum([x for x in range(3,1000) if x%3==0 or x%5==0]))


print (sum(x for x in range(3,1000) if x%3==0 or x%5==0))

print timeit.timeit("sum(x for x in range(3,1000) if x%3==0 or x%5==0)",number=1)



def mulGen():
        
    for i in [x for x in range(3,1000) if x%3==0 or x%5==0]:
        yield i

def sum1():    
    sum1=0
    for s in mulGen():
        sum1=sum1+s
    print sum1

sum1()






@timeme
def sum2():
    sum2=0
    for s in mulGen():
        sum2=sum2+s
    print sum2


sum2()
sum2()
sum2();sum2();sum2();sum2()

