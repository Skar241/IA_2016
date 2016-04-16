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

def test(p,p1,stop,heuristic):
	k = int(input("insert the value of max depth (DLS & DFBB): "))
	input("Press Enter key to init: ") 

	for i in range(1,7):
		print ("\n"+titles[i])
		startTime = time()
		if(i == 1 or i == 6):
			solution = algoritms[i](p,stop,heuristic)
		elif(i==3 or i == 4):
			solution = algoritms[i](p,stop,k)
		elif (i == 5):
			solution = algoritms[i](p,stop)
		else:
			solution = algoritms[i](p,p1)
		elapsedTime = time() - startTime
		if(solution[0]):
			print (solution[0])
			print("General stats of: "+titles[i])
			print ("Number of steps: "+str(len(solution[0])-1))
			print("Max nodes in agenda+expanded list: "+str(solution[1]+len(solution[0])-1))
		else:
			print("Gerneral stats of: "+titles[i])
			print ("solution was not found ")
		print("Elapsed time: "+str(elapsedTime)+" seconds ")
		input("Press Enter key to continue: ")


"""
p = Puzzle()
stop = lambda n: n == Puzzle()
heuristic = lambda h : ManhattanDistance().distance_to_target(h)
p.shuffle(int(input("Insert the numer of movements: ")))
print ("Puzzle to find a solution: ")
print (p)
test(p,Puzzle(),stop,heuristic)
"""

heuristic = lambda h : -ManhattanDistance().distance_to_target(h)*100
depth=int(input("\nsolution depth (positive integer): "))
stop = lambda n: heuristic(n) <=-depth*100
print ("wait, the program is searching a puzzle using A*")
tmp = algoritms[1](Puzzle(),stop,heuristic)

inicio=tmp[0][-1]
print ("Puzzle to find (depth "+str(depth)+"): \n"+str(inicio))

"""
search configurations
"""
inicio.parent=None
inicio.depth=0
stop=lambda n: n == Puzzle()
heuristic=lambda h: ManhattanDistance().distance_to_target(h)
test(inicio,Puzzle(),stop,heuristic)

