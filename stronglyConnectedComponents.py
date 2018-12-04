# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:57:11 2018

@author: rm_an
"""

import DepthFirstSearch

def scc(G):
    G.dfs()
    sortedkeys = G.orderOfFinish()
    Gt = G.transpose()
    Gt.dfsOofFinish(sortedkeys)    
    Gt.printPaths(sortedkeys)
    

G = DepthFirstSearch.dfsGraph()    

G.addEdge("A", "B")
G.addEdge("B", "E")
G.addEdge("B", "C")
G.addEdge("E", "D")
G.addEdge("E", "A")
G.addEdge("D", "B")
G.addEdge("D", "G")
G.addEdge("G", "E")
G.addEdge("C", "C")
G.addEdge("C", "F")
G.addEdge("F", "H")
G.addEdge("I", "F")
G.addEdge("H", "I")

scc(G)


    
    
    