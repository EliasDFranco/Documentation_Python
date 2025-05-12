class CuentaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor > 0:
            self._saldo = valor
        else: 
            raise ValueError("El saldo debe de ser mayor a 0, no negativo")
        
    @saldo.deleter
    def saldo(self):
        print("El saldo ha sido eliminado correctamente")
        del self._saldo
        
x = CuentaBancaria("Elias", 200)
print(x.saldo)
x.saldo = 300
print(x.saldo)
del x.saldo 
