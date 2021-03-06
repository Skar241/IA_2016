# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Created on Fri Apr 25 19:59:51 2016

@author: skar

Python version 3

Algoritmo de Busqueda A*, implementado para un puzzle de 15 piezas
Ejecucion:
	p = Puzzle()
	p.shuffle(10)
	solucion = Aestrella.search(p,lambda n: n == Puzzle(),
					lambda h: ManhattanDistance().distance_to_target(h))
	print (solucion)
"""

import queue
from search import trajectory

class Aestrella:

	def search(start,stop,heuristic):
		agenda = queue.PriorityQueue()
		explored = set() #tabla hash
		memoria = 1
		if(stop(start)):
			return (trajectory(start),memoria)

		agenda.put((0,start))
		
		while (not agenda.empty()):
			nodo = agenda.get()
			if(stop(nodo[1])):
				return (trajectory(nodo[1]),memoria)
				
			explored.add(nodo[1])
			for child in nodo[1].expand():
				if(not child in explored):
					agenda.put((child.depth+heuristic(child),child))
					if(agenda.qsize()>memoria):
						memoria=agenda.qsize()
		return (False,0)			
