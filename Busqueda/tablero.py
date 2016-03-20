# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 02:12:58 2016

@author: stan
"""
from functools import reduce

class Fifteen_Puzzle:
    
    seq = list(range(0,16))
    
    actions = ['E','W','N','S']
    
    def __init__(self, parent=None, action =None):
        self.parent = parent
        if(parent == None):
            self.configuration =  \
                reduce(lambda x,y: x | (y << 4*(y-1)), self.seq) 
            self.zero = 15
        else:
            self.configuration = parent.configuration
            self.zero = parent.zero
            if(action != None):
                self.move(action)
                
    def __str__(self):
        return ''.join(list(map(lambda i:\
        format(((self.configuration&(15<<(4*i)))>>(4*i))," x")+\
        ('\n' if (i+1)%4==0 else ''),self.seq)))
        
    def __repr__(self):
        return self.__str__()
    
    def move(self,action):
        if(action =='E'):
            self.move_east()
        if(action =='W'):
            self.move_west()
        if(action =='N'):
            self.move_north()
        if(action =='S'):
            self.move_south()
        return self
        
    def move_east(self):
        if(not self.on_right_column()):
            self.zero += 1;
            mask = (15<<(4*self.zero))
            self.configuration = \
            (self.configuration&mask)>>4 | \
            (self.configuration&~mask)
            
    def move_west(self):
        if(not self.on_left_column()):
            self.zero -= 1;
            mask = (15<<(4*self.zero))
            self.configuration = \
            (self.configuration&mask)<<4 | \
            (self.configuration&~mask)  
            
    def move_north(self):
        if(not self.on_top_row()):
            self.zero -= 4;
            mask = (15<<(4*self.zero))
            self.configuration = \
            (self.configuration&mask)<<16 | \
            (self.configuration&~mask)
            
    def move_south(self):            
        if(not self.on_bottom_row()):
            self.zero += 4;
            mask = (15<<(4*self.zero))
            self.configuration = \
            (self.configuration&mask)>>16 | \
            (self.configuration&~mask)   
            
    def on_left_column(self):
        return (self.zero%4)==0
        
    def on_right_column(self):
        return (self.zero%4)==3
        
    def on_top_row(self):
        return self.zero<=3
        
    def on_bottom_row(self):
        return self.zero>=12

    def expand(self):
        return list(filter(lambda x: (x.configuration!=self.configuration), \
        [Fifteen_Puzzle(self,action) for action in self.actions]))
    