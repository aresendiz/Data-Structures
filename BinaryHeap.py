# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:24:30 2018

@author: rm_an
"""

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
          
    def insert(self, key):
        self.heapList.append(key)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
          
    def percDown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i] 
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
            
    def minChild(self, i):
        if 2*i+1 > self.currentSize:
            return 2*i
        elif self.heapList[2*i+1]> self.heapList[2*i]:
            return 2*i
        else: 
            return 2*i+1
        
    def delMin(self):
        minval = self.heapList(1)
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return minval
    
    def buildHeap(self, alist):
        i = len(alist)//2
        self.currentSize = len(alist) + 1
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i=i-1
            