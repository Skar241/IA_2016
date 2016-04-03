# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 23:08:34 2016

@author: Gaboox
"""

from search import trajectory

class DFBB:
    
    def searchDLS(start,stop,cota):
        agenda = []
        explored = set()
        if(stop(start)):
            return trajectory(start)
        agenda.append(start)
        while(agenda):
            nodo = agenda.pop()
            explored.add(nodo)
            for child in nodo.expand():
                if(stop(child)):
                    return trajectory(child)
                elif(not child in explored and cota > child.depth):
                    agenda.append(child)

        return false
        
    def searchDFBB(start,stop,cota):
        solucion = searchDLS(start,stop,cota)
        while (solucion):
            best = solucion
            solucion = searchDLS(start,stop,cota)
            cota -= cota
        solucion = best
        print ("The solution was found with k = "+str(cota))
        return solucion
                
            
        
        
        