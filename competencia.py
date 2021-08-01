# -*- coding: utf-8 -*-
"""
CHALLENGE - JUEGO DE CARROS POR CONSOLA

----------CONSIDERACIONES-------------
1. Cada carrera finalizada se almacena en su respectivo csv con el podio de ganadores de dicha carrera.
2. Las victorias de cada jugador se acumulan mientras el programa continue en ejecución.
3. No se permite crear dos jugadores con igual nombre.
4. Para el caso del color del vehículo si es posible repetir.
5. Se requieren mínimo 3 participantes para iniciar una carrera.
6. La distancia preestablecida de la pista es de 1Km.

Created on Jul 2021
Versión 1.0
@author: Johan Toloza
"""
from carro import *
from pista import *
import os
from random import randint
import pandas as pd

iniciar = False
jugadores = []
podio = []
nCarrera = 1

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
Pista=pista(1)

def listarJugadores(lista, almacenar):
    posicion = []
    nombres = []
    colores = []
    distancia = []
    victorias = []
    cc = 0
    for i in lista:
        cc+=1
        posicion.append(cc)
        nombres.append(i.getNombre())
        colores.append(i.getColor())
        distancia.append(i.getDistancia())
        victorias.append(i.getVictorias())
    competidores = {'Nombre': nombres,
                    'Color': colores,
                    'Distancia': distancia,
                    'N. Victorias': victorias}
    datos = pd.DataFrame(competidores, index=posicion)
    print(datos)
    print()
    if(almacenar):
        datos.to_csv('Resultados_competencia_'+str(nCarrera)+'.csv')
        print()
        print("¡¡¡información de carrera almacenada correctamente!!!")
        print("-----------------------------------------------------")
        print()

def limpiarDatos(lista):
    global podio, nCarrera
    for i in lista:
        i.setDistancia(0)
    podio = []
    nCarrera += 1
        
def mensaje(text): 
    print("****************************************") 
    print("*                                      *")
    print("*  ¡",text,"!  *")
    print("*                                      *")
    print("****************************************")
    print()
    
def configurarJuego():
    while(iniciar==False):
        print("Ingrese 1 si desea añadir un participante")
        print("Ingrese 2 si desea modificar la distancia de carrera (Km)")
        print("Ingrese 3 si desea iniciar la carrera")
        print("Ingrese 4 si desea ver la lista de participantes")
        opcion = input("Ingrese la opción: ")
        print()
        
        if(opcion=="1"):
            crearJugador = True
            print("Ingrese un nombre y un color para el vehículo")
            nombreJugador = input("Ingrese su nombre: ")
            for i in jugadores:
                if(i.getNombre()==nombreJugador):
                    print("El ID ", nombreJugador, " ya se encuentra creado")
                    print()
                    crearJugador = False
                    break
            if(crearJugador):
                colorJugador = input("Ingrese un color: ")
                jugadores.append(carro(nombreJugador, colorJugador))
                print("¡¡¡se ha creado el jugador con exito!!!")
                print()
            
        elif(opcion=="2"):
            while(True):
                distancia = int(input("Ingrese la distancia de carrera (Km): "))
            
                if distancia>0: 
                    Pista.setRecorrido(distancia)
                    break
                print("Por favor ingrese un valor válido")
                print()
                
        elif(opcion=="3"):
            if len(jugadores)>2:
                break
            print("Por favor registre mínimo tres jugadores")
            print()
            
        elif(opcion=="4"):
            mensaje("LISTADO DE JUGADORES")
            listarJugadores(jugadores, False)
            
        else:
            print("\n"*10)
            clearConsole()
            print("Por favor ingrese una opcion válida")
            
def iniciarJuego():
    listarJugadores(jugadores, False)
    avanzar = True
    while(len(podio)<3):
        for i in jugadores:
            if i.getDistancia() >= Pista.getRecorrido()*1000:  
                avanzar = False
            else:
                avanzar = True                
            if (avanzar):
                print("Jugador:", i.getNombre())
                lanzar = input("Presione enter para lanzar el dado")
                distancia = randint(1, 6)*100
                i.addDistancia(distancia)
                if i.getDistancia() >= Pista.getRecorrido()*1000:              
                    i.setDistancia(Pista.getRecorrido()*1000)
                    podio.append(i)
            print()
            print("Resultados preliminares")
            listarJugadores(jugadores, False)
            print("---------------------------------------------")
            print()
            if(len(podio)>=3):
                podio[0].addVictorias()
                break

while(True):
    mensaje("JUEGO DE CARROS POR CONSOLA")
    configurarJuego()
    mensaje("INICIANDO COMPETENCIA")
    iniciarJuego()
    mensaje("PODIO DE GANADORES")
    listarJugadores(podio, True)
    limpiarDatos(jugadores)
    continuar = input('¿Desea continuar con otra carrera? S/N: ')
    if(continuar=='n' or continuar=='N'):
        break