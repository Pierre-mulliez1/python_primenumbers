# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def prime(n):
    #!!! function to determin the number of primes in a number, organised in a dict !!!
    lll = []
    l = [1, 2]
    for p in range(1, n):
        ll = []
        for q in range(2, p):
            y = p/q
            ll.append(y)
        if all(t % 1 for t in ll) == True:
            l.append(p)  
    for x in range(0,len(l)):
        try:
            if l[x] != l[x-1]:
                lll.append(l[x])
        except:
            break    
    d = { i : lll[i] for i in range(0, len(lll) ) }
    return d
print(prime(20))




