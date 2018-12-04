# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:17:33 2018

@author: rm_an
"""

class Stack:
    
    def __init__(self):
        self.items=[]
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)        
    

class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)            
    
class Deque:
# Completed implementation of a deque ADT
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):   
        self.items.append(item)
        
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def remove_front(self):
        return self.items.pop()
        
    def remove_rear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
class Node:
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_data):
        self.next = new_data
        
class UnorderedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp=Node(item)
        temp.set_next(self.head)
        self.head=temp
        if self.head.get_next() == None:
            self.tail = self.head
        
    def size(self):
        
        current = self.head
        count=0
        
        while current != None:
            count += 1
            current=current.get_next()
            
        return count
    
    def search(self, item):
        
        current= self.head
        
        while current != None:
            if current.get_data() == item:
                return True
            
            current = current.get_next()
            
        return False
    
    def remove(self, item):
        
        previous = None
        current = self.head
        
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
                
            else:
                previous = current
                current = current.get_next()
                
        if found and self.tail == self.head:
            self.head = current.get_next()
            self.tail = self.head
            
        elif found and current == self.head and current != self.tail:
            self.head = current.get_next()
            
        elif found and previous != None and current != self.tail:
            previous.set_next(current.get_next())
              
        elif found and current == self.tail and previous != None:
            previous.set_next(current.get_next()) 
            self.tail = previous
            
        else:
            print('item not in list')
            
    def append(self, item):
        
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.tail = self.head
            
        else:
            self.tail.set_next(temp)
            self.tail = temp
            
    def index(self, item):
        
        current= self.head
        count=0
        while current != None:
            if current.get_data() == item:
                return count
            
            count+=1
            current = current.get_next()
            
        return False
    
    def insert(self, index, item):
        
        temp = Node(item)
        current = self.head
        count = 0
        found = False
        
        if  index == 0:
            self.add(item)
            found=True  
        
        else:
        
            while not found and current != self.tail:                     
                
                if count == index-1:
                   temp.set_next(current.get_next())
                   current.set_next(temp)
                   found = True
                
                else:
                    count+=1
                    current = current.get_next()
        
            if current == self.tail:
                self.append(item)
          
    def pop(self, index):
        
        previous = None
        current = self.head
        count = 0
        found = False
        
        while not found:
            if count == index:
                found = True
                
            else:
                count+=1
                previous = current
                current = current.get_next()
                
        if found and self.tail == self.head:
            self.head = current.get_next()
            self.tail = self.head
            return current.get_data()
            
        elif found and current == self.head and current != self.tail:
            self.head = current.get_next()
            return current.get_data()
            
        elif found and previous != None and current != self.tail:
            previous.set_next(current.get_next())
            return current.get_data()
              
        elif found and current == self.tail and previous != None:
            previous.set_next(current.get_next()) 
            self.tail = previous
            return current.get_data()
                  
            
            
                
            
        
            
