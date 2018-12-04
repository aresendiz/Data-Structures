# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:52:31 2018

@author: rm_an
"""
from ADT import * 

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)
        
def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)
    

def move_tower_stacks(height, from_pole=None, to_pole=None, with_pole=None):
    if from_pole == None:
        from_pole=initial_pole(height)
        to_pole=Stack()
        with_pole=Stack()
    
    if height >= 1:
        move_tower_stacks(height - 1, from_pole, with_pole, to_pole)
        move_disk_stack(from_pole, to_pole, with_pole)
        move_tower_stacks(height - 1, with_pole, to_pole, from_pole)
    
    
def move_disk_stack(fp,tp,wp):    
    tp.push(fp.pop())
    print(fp.items, wp.items,tp.items) 
    
def initial_pole(height):
    pole=Stack()
    pole.items=[i for i in range(1, height+1)]
    initial_pole=Stack()
    for j in range(height):
        initial_pole.push(pole.pop())
    return initial_pole
    
    
move_tower_stacks(4)  
       
        
