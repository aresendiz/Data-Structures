# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 08:39:03 2018

@author: rm_an
"""

from ADT import *
import random

def pal_checker(a_string):
    
    char_deque=Deque()
    
    for ch in a_string:
        char_deque.add_rear(ch)
        
    while char_deque.size() > 1:
        rear=char_deque.remove_rear()
        front=char_deque.remove_front()
        
        if rear!=front:
            return False
        
    return True
        
def hotPotatoRandom(A):
    
    cycle=Queue()
    for a in A:
        cycle.enqueue(a)
    n=cycle.size()
        
    while cycle.size()>1:
        num=random.randrange(1, 2*n+1)
        for i in range(num-1):
            cycle.enqueue(cycle.dequeue())
            
        cycle.dequeue()
    
    print(cycle.items)
        
hotPotatoRandom(['Ana', 'Bob', 'Liz', 'Jay', 'Jim', 'Rose', 'Alex', 'Mac', 'Mary'])        
