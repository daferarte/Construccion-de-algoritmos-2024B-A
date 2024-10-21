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
    
    __method__='CambiarNombre'
    __params__='nombre'
    __returns__='Nada'
    __descriptions__='Este metodo modifica el nombre'
    def CambiarNombre(self, nombre):
        self.__nombre = nombre
    
    __method__='DarTipo'
    __params__='Ninguno'
    __returns__='tipo'
    __descriptions__='Este metodo retorna el tipo del producto'
    def DarTipo(self):
        return self.__tipo
    
    __method__='CambiarTipo'
    __params__='tipo'
    __returns__='Nada'
    __descriptions__='Este metodo modificar el tipo del producto'
    def CambiarTipo(self, tipo):
        self.__tipo=tipo
    
    __method__='DarValorUnitario'
    __params__='Ninguno'
    __returns__='valorUnitario'
    __descriptions__='Este metodo retorna el valorUnitario del producto'
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__='CambiarValorUnitario'
    __params__='valorUnitario'
    __returns__='Nada'
    __descriptions__='Este metodo retorna el valorUnitario del producto'
    def CambiarValorUnitario(self, valorUnitario):
        self.__valorUnitario = valorUnitario
    
    __method__='DarCantidadBodega'
    __params__='Ninguno'
    __returns__='cantidadBodega'
    __descriptions__='Este metodo retorna la cantidadBodega del producto'
    def DarCantidadBodega(self):
        return self.__cantidadBodega
    
    __method__='CambiarCantidadBodega'
    __params__='cantidadBodega'
    __returns__='Nada'
    __descriptions__='Este metodo modifica la cantidad en bodega para un producto'
    def CambiarCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega
    
    __method__='DarCantidadMinima'
    __params__='Ninguno'
    __returns__='cantidadMinima'
    __descriptions__='Este metodo retorna la cantidadMinima del producto'
    def DarCantidadMinima(self):
        return self.__cantidadMinima
    
    __method__='CambiarCantidadMinima'
    __params__='cantidadMinima'
    __returns__='Nada'
    __descriptions__='Este metodo modifica la cantidad minima del producto'
    def CambiarCantidadMinima(self, cantidadMinima):
        self.__cantidadMinima = cantidadMinima
    
    __method__='DarCantidadUnidadesVendidas'
    __params__='Ninguno'
    __returns__='cantidadUnidadesVendidas'
    __descriptions__='Este metodo retorna la cantidadUnidadesVendidas del producto'
    def DarCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
    __method__='CambiarCantidadUnidadesVendidas'
    __params__='cantidadUnidadesVendidas'
    __returns__='Nada'
    __descriptions__='Este metodo modifica la cantidad de unidades vendidas'
    def CambiarCantidadUnidadesVendidas(self, cantidadUnidadesVendidas):
        self.__cantidadUnidadesVendidas = cantidadUnidadesVendidas
    
    __method__='CalcularPrecioSupermercador'
    __params__='Ninguno'
    __returns__='precioSupermercado'
    __descriptions__='Este metodo calcula el precio del supermercado'
    def CalcularPrecioSupermercador(self):
        
        # self.__precio = self.__precio + (self.__precio * self.IVA_SUPERMERCADO)
        # self.__precio = self.__precio + (self.__precio * constantes.IVA_SUPERMERCADO)
        
        self.__precio = self.__valorUnitario+(self.__valorUnitario * constantes.IVA_SUPERMERCADO)
        
    __method__='DarPublicidad'
    __params__='Ninguno'
    __returns__='la publicidad de un producto'
    __descriptions__='Este metodo permite mostrar el nombre y el precio de un valor con un mensaje publicitario'
    def DarPublicidad(self):
        
        #return "Compre el producto "+self.__nombre+" por solo $"+self.__valorUnitario
    
        return f'Compre el producto {self.__nombre} por solo ${self.__valorUnitario}'
    
    __method__='EsIgual'
    __params__='Producto Buscado'
    __returns__='Si es el producto o no es el producto'
    __descriptions__='Este metodo permite comparar el parametro ingresado con el producto y verificar si es el mismo producto'
    def DarPublicidad(self, productoBuscado):
        return self.__nombre is productoBuscado
    
    __method__='Vender'
    __params__='cantidad a vender'
    __returns__='Nada'
    __descriptions__='Este metodo permite vender la cantidad digitada de producto'
    def Vender(self, cantidad:int):
        
        if cantidad > self.DarCantidadBodega():
            self.__cantidadUnidadesVendidas += self.DarCantidadBodega()
            self.__cantidadBodega = 0
        else:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad
    
    __method__='AgregarNuevaUnidadBodega'
    __params__='Ninguno'
    __returns__='Nada'
    __descriptions__='Este metodo permite Agregar un producto en bodega'
    def AgregarNuevaUnidadBodega(self):
        #self.__cantidadBodega+=1
        self.CambiarCantidadBodega(self.DarCantidadBodega()+1)
        
    
    __method__='Pedir'
    __params__='Cantidad pedido'
    __returns__='Nada'
    __descriptions__='Este metodo permite realizar un pedido de un producto'
    def Pedir(self, cantidad):
        #self.__cantidadBodega += cantidad
        #self.__cantidadBodega = self.__cantidadBodega+cantidad
        self.CambiarCantidadBodega(self.DarCantidadBodega()+cantidad)
    
    __method__='HaySuficiente'
    __params__='cantidad a vender'
    __returns__='Si hay suficientes elementos para vender'
    __descriptions__='Este metodo permite evaluar si la cantidad de elementos a vendder son suficientes'
    def HaySuficiente(self, cantidad:int):
        # Forma1
        # suficiente:bool = None
        
        # if(cantidad <= self.DarCantidadBodega()):
        #     suficiente=True
        # else:
        #     suficiente=False
        
        # return suficiente
        
        # Forma2
        
        # if cantidad <= self.DarCantidadBodega():
        #     return True
        # else:
        #     return False
        
        # Forma3
        
        # suficiente=False
        
        # if cantidad <= self.DarCantidadBodega():
        #     suficiente=True
        
        # return suficiente
    
        # Forma4
        
        return cantidad<= self.DarCantidadBodega()
    
    __method__='DarPrecioPapeleria'
    __params__='conIva'
    __returns__='El precio de papeleria con o sin iva'
    __descriptions__='Este metodo permite calcular el precio de un producto con iva o sin iva'
    def DarPrecioPapeleria(self, conIva:bool):
        
        precioFinal = self.DarValorUnitario()
        
        if conIva:
            precioFinal = precioFinal * ( 1+ self.IVA_PAPELERIA)
        
        return precioFinal
    
    __method__='AjustarPrecio'
    __params__='Ninguno'
    __returns__='Nada'
    __descriptions__='Este metodo permite ajustar el precio de un producto que se vende menos de cien unidades al 80% y mas de cien veces le sube el 10%'
    def AjustarPrecio(self):
        if self.DarCantidadUnidadesVendidas() < 100:
            self.__valorUnitario=self.__valorUnitario*80/100
        else:
            self.__valorUnitario=self.__valorUnitario*1.1
    
    
    __method__='DarIva'
    __params__='Ninguno'
    __returns__='Iva del producto'
    __descriptions__='Este metodo permite retornar el iva del producto'
    def DarIva(self):
        if self.DarTipo() == Tipo.FARMACIA:
            return self.IVA_FARMACIA
        elif self.DarTipo() == Tipo.PAPELERIA:
            return self.IVA_PAPELERIA
        else:
            return self.IVA_SUPERMERCADO