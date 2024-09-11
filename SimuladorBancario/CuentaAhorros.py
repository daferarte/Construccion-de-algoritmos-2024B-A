__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class CuentaAhorros:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __saldo = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    __method__='ConsignarValor'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo consignar un monto a la cuenta'
    def ConsignarValor(self, monto):
        self.__saldo=self.__saldo+monto
        
    __method__='DarSaldo'
    __params__='Ninguno'
    __returns__='Saldo'
    __descriptions__='Este metodo retorna el saldo'
    def DarSaldo(self):
        return self.__saldo
    
    __method__='RetirarValor'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo retira un monto a la cuenta'
    def RetirarValor(self, monto):
        self.__saldo=self.__saldo-monto