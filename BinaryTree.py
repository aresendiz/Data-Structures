# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:41:55 2018

@author: rm_an
"""

class BinaryTree:
    
    def __init__(self, newNode):
        self.key = newNode
        self.leftChild = None
        self.rightChild = None
        
    def insertLeftChild(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
            
        else:
            t=BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
            
        else:
            t=BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t     
            
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key    
        