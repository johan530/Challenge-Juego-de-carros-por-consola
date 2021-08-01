# -*- coding: utf-8 -*-
"""
Created on Jul 2021
Versión 1.0
@author: Johan Toloza

"""

class pista:
    def __init__(self,km):
        self.km=km
    def getRecorrido(self):
        return self.km
    def setRecorrido(self, distancia):
        self.km=distancia 