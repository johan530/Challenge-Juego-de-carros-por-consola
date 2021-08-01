# -*- coding: utf-8 -*-
"""
Created on Jul 2021
Versión 1.0
@author: Johan Toloza
"""

class carro:
    def __init__(self, nombre, color):
         self.nombre = nombre         
         self.color = color
         self.distancia=0
         self.victorias=0
    def getNombre(self):
        return self.nombre
    def getColor(self):
        return self.color
    def getDistancia(self):
        return self.distancia
    def getVictorias(self):
        return self.victorias
    def addDistancia(self, avanzar):
        self.distancia=self.distancia+avanzar
        print("Haz avanzado: ",avanzar, "m")
    def setDistancia(self, dist):
        self.distancia=dist
    def addVictorias(self):
        self.victorias=self.victorias+1
                
        