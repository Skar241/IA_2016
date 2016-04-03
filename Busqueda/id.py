"""
@author:Pérez Villarreal Guillermo
"""
from collections import deque
from search import trajectory

class ID:

    @staticmethod    
    def search(start,stop):
        agenda=deque()
        explored=set()
        if(stop(start)):
            return trajectory(start)
        agenda.append(start)
        depth=1
        while(True):
            while(agenda):
                nodo=agenda.pop()
                explored.add(nodo)
                for child in nodo.expand():
                    if(stop(child)):
                        return trajectory(child)
                    elif(not child in explored and child.depth<depth-1):
                        agenda.append(child)
            depth+=1
            agenda=deque()
            explored=set()
            agenda.append(start)

