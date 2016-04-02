# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 23:08:34 2016

@author: Gaboox
"""

from search import trajectory

class BranchAndBound:

    def search(start, stop, puzzle):
        actions = ['E','W','N','S']
        costo = set()
        hijo = set()
        nodoini = set(puzzle)
        nodo_recorrido = queue.PriorityQueue()
        nodo_vivo = queue.PriorityQueue()
        nodo_recorrido.add(nodoini)
        nodo_vivo.add(nodoini)
        
        while(nodo_vivo != empty)
            eNodo = nodo_vivo.pop()
            nHijo = eNodo.hijo(actions)
            if(nHijo != null & !nodo_recorrido(nHijo))
                if(nHijo.costo() == 0)
                    return nHijo
                else:
                    
                    nodo_vivo.add(nHijo)
                    nodo_recorrido.add(nHijo)
        return nodo_recorrido
                
            
        
        
        