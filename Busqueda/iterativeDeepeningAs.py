# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Creado el: 25 de marzo de 2016
@author:


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
		cota = heuristic(start)
		while (cota):
			agenda.put((0,start))
			while (agenda):
				nodo = agenda.get()
				if(stop(nodo[1])):
					return trajectory(nodo[1])
				explored.add(nodo[1])
				for child in nodo[1].expand():
					if(not child in explored):
						if(cota >= child.depth+heuristic(child)):
							agenda.put((child.depth+heuristic(child),child))
			cota = cota + 1
			
