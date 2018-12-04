# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:13:53 2018

@author: rm_an
"""

def SelectionSort(alist):
    
    for pos in range(len(alist),0, -1):
        index = 0
        for i in range(pos-1):
            if alist[i+1] >= alist[index]:
                index=i+1
        temp = alist[index] 
        alist[index] = alist[pos-1]
        alist[pos-1] = temp
        

                
                
alist = [54,26,93,17,77,31,44,55,20]      
print(alist)

SelectionSort(alist)

print(alist)