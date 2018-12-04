# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:07:23 2018

@author: rm_an
"""
from Graph import *
from breadthFirstSearch import bfs
from traverseBFS import traverse

def createGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # Creates buckets
    for word in wfile:
        word = word[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket not in d:
                d[bucket]=[word]
            else:
                d[bucket].append(word)
                
    # Adds vertices and edges
    for key in d.keys():
        if len(d[key])>1:
            for word in d[key]:
                for word2 in d[key]:
                    if word2 != word:
                        g.addEdge(word2,word)
                        
    return g

g = createGraph('wordladder.txt')              
bfs(g, g.getVertex('sage')) 
traverse(g, g.getVertex('pall'))
                   
