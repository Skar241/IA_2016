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
gbfs.py
Greedy Best-First Search

Artificial Intellence 1766
Engineering Faculty
UNAM

@author: Stan (stalinmunoz@yahoo.com)
"""
from search import trajectory
import heapq

class GBFS:

    @staticmethod    
    def search(start,stop,heuristic):
        agenda = []
        explored = set()
        if(stop(start)):
            return trajectory(start)
        heapq.heappush(agenda,(0,start))
        while(agenda):
            nodo = heapq.heappop(agenda)[-1];
            explored.add(nodo)
            for child in nodo.expand():
                if(stop(child)):
                    return trajectory(child)
                elif(not child in explored):
                    heapq.heappush(agenda,(heuristic(child),child))
        return None

        
        