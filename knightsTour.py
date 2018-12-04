# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:52:54 2018

@author: rm_an
"""
import Graph

def generateGraph(bdsize):
    g = Graph.Graph()
    for x in range(bdsize):
        for y in range(bdsize):
            vert = coordToNodeId(x,y,bdsize)
            nbrs= genLegalMoves(x,y, bdsize)
            for i in nbrs:
                to=coordToNodeId(i[0],i[1],bdsize)
                g.addEdge(vert, to)
    return g
                
            

def genLegalMoves(x,y, bdSize):
    newMoves = []
    possDir = [(1,2), (2,1), (-1,2), (-2,1), (2,-1), 
               (1,-2), (-1,-2), (-2, -1)]
    
    for i in possDir:
        newX = x + i[0]
        newY = y + i[1]
        
        if legalMove(newX, bdSize) and legalMove(newY, bdSize):
            newMoves.append((newX, newY))
            
    return newMoves

def legalMove(x, bdSize):
    if (x < bdSize and x >= 0):
        return True
    else:
        return False
    
def coordToNodeId(x,y,bdsize):
    return (x*bdsize)+y
    
    
def knightTour(n,path,u,limit):
    u.setColor('gray')
    path.append(u)
    
    if n < limit:
        nbr = list(u.getConnections())
        done = False
        i = 0
        while i < len(nbr) and not done:
            if nbr[i].getColor() == 'white':
                done = knightTour(n+1,path,nbr[i],limit)
            i = i+1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True        
    return done
    

g=generateGraph(3)    
for ver in g.getVertices():
    print(g.getVertex(ver))       
path=[]
v=g.getVertex(2)
print(knightTour(0,path,v,8))
print([ver.getId() for ver in path])    