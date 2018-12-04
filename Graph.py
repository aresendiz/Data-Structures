# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:22:05 2018

@author: rm_an
"""
from Vertex import *

class Graph:
    
    def __init__(self):
        self.verList = {}
        self.numVertices = 0
        
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex
    
    def getVertex(self, v):
        if v in self.verList:
            return self.verList[v]
        else:
            return None

    def __contains__(self,v):
        return v in self.vertList
    
    def addEdge(self, f, t, weight=0):
        if f not in self.verList:
            nv = self.addVertex(f)
            
        if t not in self.verList:
            nv = self.addVertex(t)
            
        self.verList[f].addNeighbor(self.verList[t], weight)
        
    def getVertices(self):
        return self.verList.keys()
    
    def transpose(self):
        Gtranspose = Graph()
        for ver in self.getVertices():
            nbrs = list(self.getVertex(ver).getConnections())
            for nbr in nbrs:
                Gtranspose.addEdge(nbr.getId(), ver)
        return Gtranspose
    
    def __iter__(self):
        return iter(self.verList.values())
            
            
            
        
        
        