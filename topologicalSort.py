# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:25:34 2018

@author: rm_an
"""
import DepthFirstSearch


def topoSort(G):
    G.dfs()
    sortedVer = G.orderOfFinish()
    return sortedVer
        
        
G = DepthFirstSearch.dfsGraph()    

G.addEdge("3/4 cups of milk", "1 cup mix")
G.addEdge("1 egg", "1 cup mix")
G.addEdge("1 Tbsp oil", "1 cup mix")
G.addEdge("1 Tbsp oil", "1 cup mix")
G.addEdge("1 cup mix", "heat syrup")
G.addEdge("1 cup mix", "pour 1/4 cup")
G.addEdge("pour 1/4 cup", "turn when bubbly")
G.addEdge("heat syrup", "eat")
G.addEdge("turn when bubbly", "eat")
G.addEdge("heat griddle", "pour 1/4 cup")


print(' --> '.join(topoSort(G)))

scc(G)
    

    


