# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:35:37 2018

@author: rm_an
"""

def insertionSort(alist):
    
    for i in range(1, len(alist)):
        currentvalue = alist[i]
        pos = i
        while pos>0 and alist[pos-1]>currentvalue:
            alist[pos] = alist[pos-1]
            pos = pos-1
            
        alist[pos] = currentvalue
    
alist = [54,26,93,17,77,31,44,55,20]
print(alist)
insertionSort(alist)
print(alist)
