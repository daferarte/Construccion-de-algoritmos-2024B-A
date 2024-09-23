__author__ = "Daniel Fernando Arteaga Fajardo"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

'''----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------'''
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __cedula=''
    __nombre=''
    
    __cuentaCorriente = CuentaCorriente()
    __cuentaAhorros = CuentaAhorros()
    __cdt = CDT()
    
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    __method__='ConsignarCuentaCorriente'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo consignar un monto a la cuenta corriente'
    def ConsignarCuentaCorriente(self, monto):
        # Aqui inicia el metodo
        # self.__cuentaCorriente.saldo = self.__cuentaCorriente.saldo+monto # modo no recomendable
        self.__cuentaCorriente.ConsignarValor(monto)
        
    __method__='CalcularSaldoTotal'
    __params__='Ninguno'
    __returns__='Saldo Total'
    __descriptions__='Este metodo sumo el saldo de todas las cuentas'
    def CalcularSaldoTotal(self):
        # Aqui inicia el metodo
        # forma 1
        total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__='PasarAhorrosACorriente'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Este metodo transfiere el saldo de ahorros a corriente'
    def PasarAhorrosACorriente(self):
        saldoTemporal = self.DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)

    __method__='Ahorrar'
    __params__='monto'
    __returns__='Ninguno'
    __descriptions__ = 'Pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parámetro (suponiendo que hay suficientes fondos).'
    def Ahorrar(self, monto):
        self.__cuentaCorriente.RetirarValor(monto)
        self.__cuentaAhorros.ConsignarValor(monto)
        
    __method__='retirarAhorro'
    __params__='monto'
    __returns__='Ninguno'
    __descriptions__ = 'Retira un valor dado de la cuenta de ahorros (suponiendo que hay suficientes fondos).'

    def retirarAhorro(self, monto):
        self.__cuentaAhorros.RetirarValor(monto)

    __method__='darSaldoCorriente'
    __params__='Ninguno'
    __returns__='el saldo de la cuenta corriente'
    __descriptions__ = 'Retorna el saldo que hay en la cuenta corriente. No olvide que éste es un método de la clase CuentaBancaria.'

    def darSaldoCorriente(self):
        return self.__cuentaCorriente.DarSaldo()

    __method__='retirarTodo'
    __params__='Ninguno'
    __returns__='cantidad retirada'
    __descriptions__ = 'Retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros.'   

    def retirarTodo(self):
        total = self.__cuentaCorriente.DarSaldo() + self.__cuentaAhorros.DarSaldo()
        self.__cuentaAhorros.RetirarValor(self.__cuentaAhorros.DarSaldo())
        self.__cuentaCorriente.RetirarValor(self.__cuentaCorriente.DarSaldo())
        return 'Usted acaba de retirar '+total
    
    __method__='duplicarAhorro'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__ = 'Duplica la cantidad de dinero que hay en la cuenta de ahorros.'
    def duplicarAhorro(self):
        self.__cuentaAhorros.ConsignarValor(self.__cuentaAhorros.DarSaldo())

    