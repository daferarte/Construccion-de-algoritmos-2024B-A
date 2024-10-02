__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

import constantes
from Tipo import Tipo
class Producto:
    
    """----------------------------------------------------------------
    # Constantes
    ----------------------------------------------------------------"""
    
    IVA_PAPELERIA = 0.16
    IVA_SUPERMERCADO = 0.04
    IVA_FARMACIA = 0.12
    
    """----------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------"""
    
    def __init__(self,nombre, tipo, nValorUnitario:float, cantidadBodega, nSubsidiado:bool, nCalidad):
        
        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        self.__nombre=nombre
        self.__tipo=tipo
        self.__valorUnitario = nValorUnitario
        self.__cantidadBodega = cantidadBodega
        self.__subsidiado = nSubsidiado
        self.__calidad = nCalidad
        self.__cantidadMinima = 0
        self.__cantidadUnidadesVendidas = 0
        
    __method__='DarNombre'
    __params__='Ninguno'
    __returns__='Nombre'
    __descriptions__='Este metodo retorna el nombre del producto'
    def DarNombre(self):
        return self.__nombre
    
    __method__='DarTipo'
    __params__='Ninguno'
    __returns__='tipo'
    __descriptions__='Este metodo retorna el tipo del producto'
    def DarTipo(self):
        return self.__tipo
    
    __method__='DarValorUnitario'
    __params__='Ninguno'
    __returns__='valorUnitario'
    __descriptions__='Este metodo retorna el valorUnitario del producto'
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__='DarCantidadBodega'
    __params__='Ninguno'
    __returns__='cantidadBodega'
    __descriptions__='Este metodo retorna la cantidadBodega del producto'
    def DarCantidadBodega(self):
        return self.__cantidadBodega
    
    __method__='DarCantidadMinima'
    __params__='Ninguno'
    __returns__='cantidadMinima'
    __descriptions__='Este metodo retorna la cantidadMinima del producto'
    def DarCantidadMinima(self):
        return self.__cantidadMinima
    
    __method__='DarCantidadUnidadesVendidas'
    __params__='Ninguno'
    __returns__='cantidadUnidadesVendidas'
    __descriptions__='Este metodo retorna la cantidadUnidadesVendidas del producto'
    def DarCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    __method__='CalcularPrecioSupermercador'
    __params__='Ninguno'
    __returns__='precioSupermercado'
    __descriptions__='Este metodo calcula el precio del supermercado'
    def CalcularPrecioSupermercador(self):
        
        # self.__precio = self.__precio + (self.__precio * self.IVA_SUPERMERCADO)
        # self.__precio = self.__precio + (self.__precio * constantes.IVA_SUPERMERCADO)
        
        self.__precio = self.__valorUnitario+(self.__valorUnitario * constantes.IVA_SUPERMERCADO)