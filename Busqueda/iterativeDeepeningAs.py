# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Created on Fri Apr 25 20:29:21 2016

@author: skar

Para ver el repositorio completo puede visitar el siguiente link:
https://github.com/Skar241/IA_2016/tree/master/Busqueda

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
		if(stop(start)):
			return trajectory(start)
		cota = 1
		while (True):
			agenda.put((0,start))
			while (not agenda.empty()):
				nodo = agenda.get()
				if(stop(nodo[1])):
					return trajectory(nodo[1])
				explored.add(nodo[1])
				for child in nodo[1].expand():
					if(not child in explored):
						if(cota -1 > child.depth+heuristic(child)):
							agenda.put((child.depth+heuristic(child),child))
			cota += 1
			agenda = queue.PriorityQueue()
			explored = set()

			
