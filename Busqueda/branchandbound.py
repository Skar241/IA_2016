# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 23:08:34 2016

@author: Gaboox
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
                
            
        
        
        