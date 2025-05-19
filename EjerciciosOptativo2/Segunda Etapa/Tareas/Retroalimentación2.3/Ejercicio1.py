# Crear una clase Cuenta que permita realizar depósitos,
# retiros y mostrar el saldo.

class Cuenta:
    def __init__(self, saldoCuenta, titularCuenta):
        self._saldoCuenta = saldoCuenta
        self._titularCuenta = titularCuenta
        
    @property
    def saldoCuenta(self):
        return self._saldoCuenta
    
    @saldoCuenta.setter
    def saldoCuenta(self, valorSaldo):
        if valorSaldo >= 0: 
            self._saldoCuenta = valorSaldo
        else: 
            raise ValueError("Su saldo debe de ser mayor a 0.")

    @property
    def titularCuenta(self):
        return self._titularCuenta
    
    def depositarDinero(self, montoDeposito):
        if montoDeposito > 0: 
            self._saldoCuenta += montoDeposito
            print(f"El deposito de {montoDeposito} ha sido exitoso.")
        else:
            raise ValueError("Intente depositar un valor mayor a 0")
    
    def retirarDinero(self, montoDeposito):
        if montoDeposito <= 0:
            raise ValueError("El monto que usted quiere retirar debe de ser mayor a 0. ")
        elif montoDeposito > self._saldoCuenta:
            raise ValueError("Monto insuficiente, no puede retirar mingún monto de dinero")
        else:
            self._saldoCuenta -= montoDeposito
            print(f"El retiro de dinero ha sido exitoso.")
            
    def mostrarSaldo(self):
        print(f"Titular de la cuenta: {self._titularCuenta} . Saldo Actual: {self._saldoCuenta}")
            
c = Cuenta(10000, "Elias Franco")
c.mostrarSaldo()

print("\n")
c.depositarDinero(1000)
c.mostrarSaldo()

print("\n")
c.retirarDinero(3000)
c.mostrarSaldo()