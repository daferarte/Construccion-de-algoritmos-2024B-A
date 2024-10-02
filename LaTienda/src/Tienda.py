__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Producto import Producto
class Tienda:
    
    """----------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------"""
    __method__='Constructor'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Metodo constructor de la clase tienda'
    def __init__(self):
        
        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        self.__producto1 = None
        self.__producto2 = None
        self.__producto3 = None
        self.__producto4 = None
        
        self.__dineroCaja:float = 0
    
    """----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------"""
    
    __method__='DarProducto1'
    __params__='Ninguno'
    __returns__='Producto1'
    __descriptions__='Este metodo retorna la informacion del producto 1'
    def DarProducto1(self):
       
    __method__='DarProducto2'
    __params__='Ninguno'
    __returns__='Producto2'
    __descriptions__='Este metodo retorna la informacion del producto 2'
    def DarProducto2(self):
    
    __method__='DarProducto3'
    __params__='Ninguno'
    __returns__='Producto3'
    __descriptions__='Este metodo retorna la informacion del producto 3'
    def DarProducto3(self):
    
    __method__='DarProducto4'
    __params__='Ninguno'
    __returns__='Producto4'
    __descriptions__='Este metodo retorna la informacion del producto 4'
    def DarProducto4(self):
        
    __method__='DarDineroCaja'
    __params__='Ninguno'
    __returns__='DineroCaja'
    __descriptions__='Este metodo retorna la cantidad de dinero que existe en caja'
    def DarDineroCaja(self):
        return self.__dineroCaja