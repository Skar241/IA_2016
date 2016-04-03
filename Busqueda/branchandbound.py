# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Created on Fri Apr 01 23:08:34 2016

@author: Gaboox

Python version 3

Algoritmo de Busqueda DFBB, implementado para un puzzle de 15 piezas
Ejecucion:
    p = Puzzle()
    p.shuffle(10)
    solucion = DFBB.search(p,lambda n: n == Puzzle(),maxDepth)
    print (solucion)
"""

from dls import DLS

class DFBB:
        
    def search(start,stop,cota):
        solucion = DLS.search(start,stop,cota)
        best = False
        while (solucion):
            best = solucion.copy()
            cota -= 1
            solucion = DLS.search(start,stop,cota)
        if(best):
            print ("The solution was found with k = "+str(cota))
            return best
        else:
            return False
                
            
        
        
        