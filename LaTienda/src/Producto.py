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
    
    def __init__(self, nValorUnitario:float, nSubsidiado:bool, nCalidad):
        
        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        
        self.__valorUnitario = nValorUnitario
        self.__subsidiado = nSubsidiado
        self.__calidad = nCalidad
        self.___tipoVenta = Tipo.FARMACIA
        
        
        """----------------------------------------------------------------
        # self.__subsidiado = True
        # self.__subsidiado = False
        ----------------------------------------------------------------"""
        
        
    def CalcularPrecioSupermercador(self):
        
        # self.__precio = self.__precio + (self.__precio * self.IVA_SUPERMERCADO)
        # self.__precio = self.__precio + (self.__precio * constantes.IVA_SUPERMERCADO)
        
        self.__precio = self.__valorUnitario+(self.__valorUnitario * constantes.IVA_SUPERMERCADO)