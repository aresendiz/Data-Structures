# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 17:31:25 2018

@author: rm_an
"""

class HashTable:
    
    def __init__(self, len):
        self.size = len
        self.slots = [None]*self.size
        self.data = [None]*self.size
        
    def put(self, key, data):
        hashvalue=self.hashfunction(key, self.size)
        
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            
        elif self.slots[hashvalue] == key:
            self.data[hashvalue] == data
            
        else:
            hashvalue = self.rehash(hashvalue,self.size)
            
            while self.slots[hashvalue] != None and self.slots[hashvalue] !=key:
                hashvalue = self.rehash(hashvalue, self.size)
            
            if self.slots[hashvalue] == None:
                self.slots[hashvalue] = key
                self.data[hashvalue] = data
                
            else:
                self.data[hashvalue] = data
                
            
    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, size):
        return (oldhash+1) % size
    
    def get(self, key):
        
        startslot=self.hashfunction(key, self.size)
        stop=False
        
        if self.slots[startslot] == key:
            return self.data[startslot]
            
        else:
            hashvalue = startslot
            
            while not stop:
                hashvalue = self.rehash(hashvalue, self.size)
            
                if self.slots[hashvalue] == key:
                    return self.data[hashvalue]
                
                elif hashvalue == startslot: 
                    stop = True
                    
            return None
   
    def __delitem__(self, key):      
        
        startslot=self.hashfunction(key, self.size)
        stop = False
        found = False
        hashvalue =  startslot    
        
        while not stop and not found and self.slots[hashvalue] != None:
            
            if self.slots[startslot] == key:
                self.slots[startslot] = None
                self.data[startslot] = None
                found = True
    
            else:              
                hashvalue = self.rehash(hashvalue, self.size)
            
                if self.slots[hashvalue] == key:
                    self.slots[hashvalue] = None
                    self.data[hashvalue] = None
                    found = True
                
                elif hashvalue == startslot: 
                    stop = True
                    
    def __len__(self):
        count=0
        for slot in self.slots:
            if slot != None:
                count +=1
        return count       

    def __contains__(self, key):
        startslot=self.hashfunction(key, self.size)
        stop=False
        
        if self.slots[startslot] == key:
            return True
            
        else:
            hashvalue = startslot
            
            while not stop:
                hashvalue = self.rehash(hashvalue, self.size)
            
                if self.slots[hashvalue] == key:
                    return True
                
                elif hashvalue == startslot: 
                    return False
            
            
                    
    
    def __setitem__(self,key,data):
        self.put(key,data)
        
    def __getitem__(self,key):
        return self.get(key)
        
            
H=HashTable(11)
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots) 
print(H.data) 
print(H[54])
print(H[55])      
print(H[44])   
del H[55]
print(H.slots) 
print(H.data)         
print(55 in H)
print(44 in H)
