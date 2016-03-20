# -*- coding: utf-8 -*-
"""
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Created on Sun Feb 28 23:52:25 2016
bfs.py
Breadth-First Search

Artificial Intellence 1766
Engineering Faculty
UNAM

@author: Stan (stalinmunoz@yahoo.com)
"""
from collections import deque
from search import trajectory
class BFS:

    @staticmethod    
    def search(start,stop):
        agenda = deque()
        explored = set()
        if(stop(start)):
            return trajectory(start)
        agenda.append(start)
        while(agenda):
            nodo = agenda.popleft()
            explored.add(nodo)
            for child in nodo.expand():
                if(stop(child)):
                    return trajectory(child)
                elif(not child in explored):
                    agenda.append(child)
        return None

        
        