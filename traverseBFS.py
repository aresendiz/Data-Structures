# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:58:26 2018

@author: rm_an
"""

def traverse(graph, target):
    currentVert=target
    while currentVert.getPred():
        print(currentVert.getId())
        currentVert = currentVert.getPred()  
    print(currentVert.getId())    
    