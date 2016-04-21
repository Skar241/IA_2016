# -*- coding: utf-8 -*-
"""
Artificial Intellence 1766
Engineering Faculty
UNAM

Created on Fri Apr  1 10:19:25 2016

@author: :)

Python version 3

Algoritmo de Busqueda Bidireccional, implementado para un puzzle de 15 piezas
Ejecucion:
    p = Puzzle()
    p.shuffle(10)
    solucion = Bidireccional.search(p,Puzzle())
    print (solucion)

"""
from search import trajectory

class Bidirectional:
    
    def search(start,stop):
        Forward = set()
        Backward = set()
        Explored = set()
        Forward.add(start)
        Backward.add(stop)
        memoria1=1
        memoria2=1
        
        while (True):
            ForwardCpy = Forward.copy()
            while(ForwardCpy):
                Forward.pop()
                s = ForwardCpy.pop()
                Explored.add(s)
                if(s in Backward):
                    tmp = Backward.copy()
                    tmp2 = tmp.pop()
                    while(not s.__eq__(tmp2)):
                        tmp2 = tmp.pop()
                    traj = trajectory(tmp2)
                    traj.pop()
                    traj.reverse()
                    tmp2 = traj.pop()
                    while(not stop.__eq__(tmp2)):
                        tmp2 = traj.pop()
                    traj.append(stop)
                    return (trajectory(s)+traj,memoria1+memoria2)
                for child in s.expand():
                    if(not child in Explored):
                        Forward.add(child)
                        if(len(Forward)>memoria1):
                            memoria1=len(Forward)
            
            BackwardCpy = Backward.copy()
            while (BackwardCpy):
                Backward.pop()
                s = BackwardCpy.pop()
                Explored.add(s)
                if(s in Forward):
                    tmp = Forward.copy()
                    tmp2 = tmp.pop()
                    while(not s.__eq__(tmp2)):
                        tmp2 = tmp.pop()
                    traj = trajectory(s)
                    traj.pop()
                    traj.reverse()
                    tmp3 = traj.pop()
                    while (not stop.__eq__(tmp3)):
                        tmp3 = traj.pop()
                    traj.append(stop)
                    return (trajectory(tmp2)+traj,memoria1+memoria2)
                for child in s.expand():
                    if(not child in Explored):
                        Backward.add(child)
                        if(len(Backward)>memoria2):
                            memoria2=len(Backward)