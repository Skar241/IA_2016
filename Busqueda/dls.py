"""
@author:Pérez Villarreal Guillermo
"""
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
