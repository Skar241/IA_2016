# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Creado el: 25 de marzo de 2016
@author:


Para ver el repositorio completo puede visitar el siguiente link:
https://github.com/Skar241/IA_2016/tree/master/Busqueda

"""

import queue
from search import trajectory
from manhattan import ManhattanDistance

class IDA:

	def search(start,stop):
		agenda = queue.PriorityQueue()
		md = ManhattanDistance()
		explored = set()
		if(stop(start)):
			return trajectory(start)
		cota = md.distance_to_target(start)
		agenda.put((0,start))

		while (agenda):
			nodo = agenda.get()
			if(stop(nodo[1])):
				return trajectory(nodo[1])
			explored.add(nodo)
			for child in nodo[1].expand():
				if(not child in explored):
					if(cota >= child.depth+md.distance_to_target(child)):
						agenda.put((child.depth+md.distance_to_target(child),child))
			
