"""
Artificial Intellence 1766
Engineering Faculty
UNAM

@author:Pérez Villarreal Guillermo

Python version 3

Algoritmo de Busqueda DLS, implementado para un puzzle de 15 piezas
Ejecucion:
    p = Puzzle()
    p.shuffle(10)
    solucion = Aestrella.search(p,lambda n: n == Puzzle(),maxDepth)
    print (solucion)

"""
from collections import deque
from search import trajectory

class DLS:

    @staticmethod    
    def search(start,stop,depth):
        agenda=deque()
        explored=set()
        if(stop(start)):
            return trajectory(start)
        elif(depth==0):
            return None
        agenda.append(start)
        while(agenda):
            nodo=agenda.pop()
            explored.add(nodo)
            for child in nodo.expand():
                if(stop(child)):
                    return trajectory(child)
                elif(not child in explored and child.depth<depth-1):
                    agenda.append(child)
        return None
