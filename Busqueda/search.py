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

Created on Fri Mar  4 16:02:26 2016
search.py
Search utilities

Artificial Intellence 1766
Engineering Faculty
UNAM

@author: Stan (stalinmunoz@yahoo.com)
"""
from collections import deque

def trajectory(end):
    sequence = deque()
    sequence.append(end)
    while end.parent:
        end = end.parent
        sequence.append(end)
    sequence.reverse()
    return list(sequence)