# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

@author:Pérez Villarreal Guillermo

Python version 3

Algoritmo de Busqueda ID, implementado para un puzzle de 15 piezas
Ejecucion:
    p = Puzzle()
    p.shuffle(10)
    solucion = Aestrella.search(p,lambda n: n == Puzzle())
    print (solucion)
"""
from collections import deque
from search import trajectory

class ID:

    @staticmethod    
    def search(start,stop):
        agenda=deque()
        memoria=1
        if(stop(start)):
            return (trajectory(start),memoria)
        agenda.append(start)
        depth=1
        while(True):
            while(agenda):
                nodo=agenda.pop()
                for child in nodo.expand():
                    if(stop(child)):
                        return (trajectory(child),memoria)
                    elif(child.depth<depth-1):
                        agenda.append(child)
                        if(len(agenda)>memoria):
                            memoria=len(agenda)
            depth+=1
            agenda=deque()
            memoria=1
            agenda.append(start)

