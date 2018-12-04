# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:14:42 2018

@author: rm_an
"""

from ADT import *

def bfs(graph, start):
    
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)

    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setPred(currentVert)
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setColor('gray')
                vertQueue.enqueue(nbr)
                
        currentVert.setColor('black')
                
        
        
                