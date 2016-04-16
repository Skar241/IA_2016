from collections import deque
from search import trajectory

class DLS:

    def search(start,stop,depth):
        agenda=deque()
        explored=set()
        memoria=1
        if(stop(start)):
            return (trajectory(start),memoria)
        elif(depth==0):
            return (None,0)
        agenda.append(start)
        while(agenda):
            nodo=agenda.pop()
            explored.add((nodo,nodo.depth))
            for child in nodo.expand():
                if(stop(child)):
                    return (trajectory(child),memoria)
                elif(not((child,child.depth) in explored) and child.depth<depth-1):
                    agenda.append(child)
                    if(len(agenda)>memoria):
                        memoria=len(agenda)
        return (None,0)
