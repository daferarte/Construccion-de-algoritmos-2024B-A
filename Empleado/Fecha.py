__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Fecha:
    # Aquí inicia mi clase
    
    '''#-------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------#'''
    
    dia = 0
    mes = 0
    anio = 0
    
    '''#-------------------------------------------------------------
    # Metodos
    -------------------------------------------------------------#'''
    
    __method__='DarDia'
    __params__='Ninguno'
    __returns__='Dia de la clase'
    __descriptions__='Devuelve el dia de la clase'
    
    def DarDia(self):
        return self.dia
    
    __method__='DarMes'
    __params__='Ninguno'
    __returns__='Mes de la clase'
    __descriptions__='Devuelve el mes de la clase'
    
    def DarMes(self):
        return self.mes
    
    __method__='DarAnio'
    __params__='Ninguno'
    __returns__='Año de la clase'
    __descriptions__='Devuelve el año de la clase'
    
    def DarAnio(self):
        return self.anio
    
    __method__='DarFecha'
    __params__='Ninguno'
    __returns__='Fecha de la clase'
    __descriptions__='Devuelve la fecha de la clase'
    def DarFecha(self):
        # Aqui inicia mi metodo
        return self.dia+'/'+self.mes+'/'+self.anio
    
        
    
    