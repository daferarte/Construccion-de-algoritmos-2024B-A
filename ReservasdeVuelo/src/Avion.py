__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Silla import Silla

class Avion():
    
    # constantes
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42
    
    def __init__(self):
        
        self.__sillasEjecutivas:Silla = []
        self.__sillasEconomicas:Silla = []
        
        # creacion de sillas ejecutivas
        self.__sillasEjecutivas[0] = Silla(1, 1, 1)
        self.__sillasEjecutivas[1] = Silla(2, 1, 2)
        self.__sillasEjecutivas[2] = Silla(3, 1, 2)
        self.__sillasEjecutivas[3] = Silla(4, 1, 1)
        self.__sillasEjecutivas[4] = Silla(5, 1, 1)
        self.__sillasEjecutivas[5] = Silla(6, 1, 2)
        self.__sillasEjecutivas[6] = Silla(7, 1, 2)
        self.__sillasEjecutivas[7] = Silla(8, 1, 1)
        
        # creacion de sillas economicas
        self.creacionSillasEconomicas()
        
    __method__='creacionSillasEconomicas'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Este metodo crea las sillas economicas del avion'    
    def creacionSillasEconomicas(self):
        
        # for i in range (0,self.SILLAS_ECONOMICAS, 3):
        #     self.__sillasEconomicas[i] = Silla((i+1), 2, 1)
        #     self.__sillasEconomicas[i+1] = Silla((i+2), 2, 3)
        #     self.__sillasEconomicas[i+2] = Silla((i+3), 2, 2)
        for i in range (self.SILLAS_ECONOMICAS):
            if (i+1) % 3 == 0:
                self.__sillasEconomicas[i] = Silla((i+1), 2, 2)
            elif (i+1) % 2 == 0:
                self.__sillasEconomicas[i] = Silla((i+1), 2, 3)
            else:
                self.__sillasEconomicas[i] = Silla((i+1), 2, 1)
    
    __method__='EliminarReservas'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Este metodo elimina todas las reservas del avion'
    def  EliminarReservas(self):
        for sillaEjecutiva in self.__sillasEjecutivas:
            sillaEjecutiva.DesasignarSilla()
        
        for sillaEconomica in self.__sillasEconomicas:
            sillaEconomica.DesasignarSilla()