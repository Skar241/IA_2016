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
	k = int(input("insert the value of k: "))
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
heuristic = lambda h : -ManhattanDistance().distance_to_target(h)
#heuristica necesaria para todas las siguientes pruebas
print ("wait, the program is searching a solution for bidirectional search")
"""
stop = lambda n: heuristic(n) <=-10
tmp = algoritms[1](Puzzle(),stop,heuristic)
print ("Puzzle to find (depth 10): ")
test(Puzzle(),tmp[0][-1],stop,heuristic)

stop = lambda n: heuristic(n) <=-20
tmp = algoritms[1](Puzzle(),stop,heuristic)
print ("Puzzle to find (depth 20): ")
test(Puzzle(),tmp[0][-1],stop,heuristic)
"""
stop = lambda n: heuristic(n) <=-30
tmp = algoritms[1](Puzzle(),stop,heuristic)
print ("Puzzle to find (depth 30): ")
test(Puzzle(),tmp[0][-1],stop,heuristic)
"""  
stop = lambda n: heuristic(n) <=-40
tmp = algoritms[1](Puzzle(),stop,heuristic)
print ("Puzzle to find (depth 40): ")
test(Puzzle(),tmp[0][-1],stop,heuristic)

stop = lambda n: heuristic(n) <=-50
tmp = algoritms[4](Puzzle(),stop,52)
print ("Puzzle to find (depth 50): ")
test(Puzzle(),tmp[0][-1],stop,heuristic)
"""