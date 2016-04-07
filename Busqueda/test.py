# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Created on Sat Apr  2 19:59:51 2016

@author: skar
"""
from aEstrella import Aestrella
from bidirectional import Bidirectional
from branchandbound import DFBB
from dls import DLS
from id import ID
from iterativeDeepeningAs import IDA
from manhattan import ManhattanDistance
from puzzle import Puzzle
from time import time

algoritms = {
	1: Aestrella.search,
	2: Bidirectional.search,
	3: DFBB.search,
	4: DLS.search,
	5: ID.search,
	6: IDA.search
	}

titles = {
	1: "A*",
	2: "Bidirectional",
	3: "Depth First Branch and Bound",
	4: "Depth Limited Search",
	5: "Iterative Deepening",
	6: "Iterative Deepening A*"
	}

p = Puzzle()
stop = lambda n: n == Puzzle()
heuristic = lambda h : ManhattanDistance().distance_to_target(h)

print ("Puzzle to find a solution: ")
print (p.shuffle(20))

x = input("Press Enter key to init: ") 

for i in range(1,7):
	print ("\n"+titles[i])
	startTime = time()
	if(i == 1 or i == 6):
		solution = algoritms[i](p,stop,heuristic)
	elif(i==3 or i == 4):
		solution = algoritms[i](p,stop,heuristic(p)+1)
	elif (i == 5):
		solution = algoritms[i](p,stop)
	else:
		solution = algoritms[i](p,Puzzle())
	elapsedTime = time() - startTime
	if(solution):
		print (solution)
		print("General stats of: "+titles[i])
		print ("Number of steps: "+str(len(solution)))
	else:
		print("Gerneral stats of: "+titles[i])
		print ("solution was not found ")
	print("Elapsed time: "+str(elapsedTime)+" seconds ")
	x = input("Press Enter key to continue: ")
