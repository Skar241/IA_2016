# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:19:25 2016

@author: :)

"""
from search import trajectory

class Bidirectional:
    
    def search(start,stop):
        Forward = set()
        Backward = set()
        Explored = set()
        Forward.add(start)
        Backward.add(stop)
        
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
                    return trajectory(s)+traj
                for child in s.expand():
                    if(not child in Explored):
                        Forward.add(child)
            
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
                    return trajectory(tmp2)+traj
                for child in s.expand():
                    if(not child in Explored):
                        Backward.add(child)