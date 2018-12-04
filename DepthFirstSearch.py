# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:52:43 2018

@author: rm_an
"""
from Graph import *
class dfsGraph(Graph):
    
    def __init__(self):
        super().__init__()
        self.time = 0
    
    def dfs(self):
        for ver in self:
            ver.setColor('white')
            ver.setPred(None)
        self.time = 0
        
        for ver in self:
            if ver.getColor() == 'white':
                self.dfsVisit(ver)
                
    def dfsOofFinish(self, sortedKeys):
        for ver in self:
            ver.setColor('white')
            ver.setPred(None)
        self.time = 0
        
        sortedVer = [self.getVertex(key) for key in sortedKeys]
        
        for ver in sortedVer:
            if ver.getColor() == 'white':
                self.dfsVisit(ver)
        return sortedKeys
        
                
    def dfsVisit(self, ver):
        self.time += 1
        ver.setDiscovery(self.time)
        ver.setColor('gray')
        for nbr in ver.getConnections():
            if nbr.getColor() == 'white':
                nbr.setPred(ver)
                self.dfsVisit(nbr)
        ver.setColor('black')
        self.time += 1
        ver.setFinish(self.time)
        
    def orderOfFinish(self):
        sortedKeys = []
        for ver in self:
            sortedKeys.append((ver.getFinish(),ver.getId()))
        sortedKeys.sort(key=lambda x: x[0], reverse=True)
        return [key[1] for key in sortedKeys]
    
    def printPaths(self, sortedkeys):
        sortedkeys.reverse()
        sortedVer=[self.getVertex(key) for key in sortedkeys]
        
        for ver in sortedVer:
            if ver.getColor() == 'black':
                print (self.getPath(ver))
                
    def getPath(self, ver):
        path = []
        currentVer= ver
        currentVer.setColor('white')
        path.append(currentVer.getId())
        while currentVer.getPred():
            path.append(currentVer.getPred().getId())
            currentVer = currentVer.getPred()
            currentVer.setColor('white')
            for otherVer in self:
                if otherVer.getColor() == 'black' and otherVer.getPred():
                    if otherVer.getPred().getId() in path:
                        path.append(otherVer.getId())
                        otherVer.setColor('white')
        return path
    
    def transpose(self):
        Gtranspose = dfsGraph()
        for ver in self.getVertices():
            nbrs = list(self.getVertex(ver).getConnections())
            for nbr in nbrs:
                Gtranspose.addEdge(nbr.getId(), ver)
        return Gtranspose
                    
                    
            
            
            
        
        

        
        
    
    