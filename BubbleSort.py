# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:26:34 2018

@author: rm_an
"""

def BubbleSort(alist):
    
    for pos in range(len(alist)-1,0, -1):
        count=0
        for i in range(pos):
            if alist[i] > alist[i+1]:
                temp = alist[i+1]
                alist[i+1] = alist[i]
                alist[i] = temp
                count += 1
        if count == 0:
            break
alist= [3,4,5,7,6]       
print(alist)

BubbleSort(alist)

print(alist)
        