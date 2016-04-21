# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Created on Fri Apr 25 20:29:21 2016

@author: skar

Python version 3

Algoritmo de Busqueda IDA*, implementado para un puzzle de 15 piezas
Ejecucion:
	p = Puzzle()
	p.shuffle(10)
	solucion = IDA.search(p,lambda n: n == Puzzle(),
					lambda h: ManhattanDistance().distance_to_target(h))
	print (solucion)

"""

import queue
from search import trajectory

class IDA:

    def search(start,stop,heuristic):
        agenda = queue.PriorityQueue()
        explored = set()
        memoria = 1
        if(stop(start)):
            return (trajectory(start),memoria)
        cota = heuristic(start)
        mini = 0
        while (True):
            agenda.put((0,start))
            while (not agenda.empty()):
                nodo = agenda.get()
                if(stop(nodo[1])):
                    return (trajectory(nodo[1]),memoria)
                explored.add(nodo[1])
                for child in nodo[1].expand():
                    if(not child in explored):
                        if(cota > child.depth+heuristic(child)):
                            agenda.put((child.depth+heuristic(child),child))
                            if(agenda.qsize()>memoria):
                                memoria=agenda.qsize()
                        elif (child.depth+heuristic(child) != cota):
                            if(mini == 0 or mini > child.depth+heuristic(child)):
                                mini = child.depth+heuristic(child)
                        
            cota = mini
            agenda = queue.PriorityQueue()
            explored = set()
            memoria=1
            mini = 0

			
