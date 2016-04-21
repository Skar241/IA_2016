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
        memoria=solucion[1]
        best = (False,0)
        while(solucion[0]):
            best = solucion
            cota = solucion[0][-1].depth - 1
            solucion = DLS.search(start,stop,cota)
        if(best[0]):
            print ("The solution was found with k = "+str(cota+1))
            return (best[0],memoria)
        else:
            return (False,0)
                
            
        
        
        
