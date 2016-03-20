# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 01:30:32 2016

@author: stan
"""

def hello():
    print('Hello world!')
    
    
def say(*things,**dictio):
    for thing in things:
        print(thing)
    for key in dictio.keys():
        print(dictio[key])
        


hello()