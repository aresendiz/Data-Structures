# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 10:12:23 2018

@author: rm_an
"""

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.pred = None
        self.color = 'white'
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setDistance(self, d):
        self.distance = d
        
    def setPred(self, predecessor):
        self.pred = predecessor
        
    def setDiscovery(self, t):
        self.discovery = t
        
    def setFinish(self, t):
        self.finish = t
    
    def setColor(self, color):
        self.color = color
        
    def getFinish(self):
        return self.finish
    
    def getDiscovery(self):
        return self.discovery
        
    def getColor(self):
        return self.color
    
    def getDistance(self):
        return self.distance
    
    def getPred(self):
        return self.pred

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]