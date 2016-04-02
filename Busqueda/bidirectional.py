# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:19:25 2016

@author: :)

"""



from search import trajectory

class Bidirectional:

    def search(start,stop):
        Forward = set()
        Backward =set()
        Forward.add(start)
        Backward.add(stop)
        
        #while ():
        while(Forward):
            s = Forward.pop()
            tmp = Backward.copy()              
            while(tmp):
                tmp2 = tmp.pop()
                if(s.configuration == tmp2.configuration):
                    return trajectory(s)+trajectory(tmp2)
                for child in s.expand():
                    if(not child in Forward):
                        Forward.add(child)
        while (Backward):
            s = Backward.pop()
            tmp = Forward.copy()
            while(tmp):
                tmp3 = tmp.pop()
                if(s.configuration == tmp3.configuration):
                    return trajectory(tmp3)+trajectory(s)
                for child in s.expand():
                    if(not child in Backward):
                        Backward.add(child)