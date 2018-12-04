# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:19:55 2018

@author: rm_an
"""

from ADT import Stack
from BinaryTree import *
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    
    for i in fplist:
        
        if i == '(':
            currentTree.insertLeftChild('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
            
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRightChild('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
                           
        elif i == ')':
            currentTree = pStack.pop()
            

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                currentTree = pStack.pop()
                
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
    



                
                
            
                       