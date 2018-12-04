# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:54:28 2018

@author: rm_an
"""
from parseTree import buildParseTree

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
pt = buildParseTree("( ( 10 + 5 ) * 3 )")

print(preorder(pt))

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

print('')
print(postorder(pt))        

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())
      
print('')
print(inorder(pt))         

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

print('')
print(printexp(pt)) 

