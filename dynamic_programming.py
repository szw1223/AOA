# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# a rotated sorted array is a clever transformation.撒旦飞洒地方撒旦发射点发生
#def cutbottomup(n):
#    p = [0,1,5,8,9,10,17,17,20,24,30]
#    p = p + [0] * (n - len(p) + 1)
#    pf = [0] * (n + 1)
#
#    for i in range(1, n + 1):
#        
#        if n == 0:
#            return 0
#            
#        pcurrent = []
#        for j in range(1, (i + 1)):
#            pcurrent.append(p[j] + pf[i - j])
#        pf[i] = max(pcurrent)
#        
#    return pf[n], pf
#    
#print(cutbottomup(15))

def cutbottomup(n):
    p = [0,1,5,8,9,10,17,17,20,24,30]
    p = p + [0] * (n - len(p) + 1)
    pf = [0] * (n + 1)
    
    for i in range(1, n + 1):
        
        if n == 0:
            return 0
        f = -1000   
        for j in range(1, (i + 1)):
            if f < p[j] + pf[i - j]:
                
                f = p[j] + pf[i - j]
                pf[i] 
        
    return pf[n]
    
print(cutbottomup(150))


def pt_1(n):
    p = [0,1,5,8,9,10,17,17,20,24,30]
    p = p + [0] * (n - len(p) + 1)
    pf = [0] * (n + 1)
    
    
def cut(n):
    p = [0,1,5,8,9,10,17,17,20,24,30]
    p = p + [0] * (n - len(p) + 1)
    pf = [0] * (n + 1)
    if n == 0:
        return 0
    q = -1000
    for i in range(1, n + 1):
        q = max(q, p[i] + cut(n - i))
    return q
print(cut(15))


def matrix_min(a, b):
    for i in range(1, len(a) + 1):
        c[i] = [b[i], b[i + 1]]
    print(c)

a = range(1, 11)
b = [12, 23, 21, 10, 100, 40, 5, 1, 30, 12, 3, 60]
c = {}
