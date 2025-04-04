class CuentaBancaria:
    def __init__(self, titular, saldo, tipoCuenta):
        self.titular = titular
        self.saldo = saldo
        self.tipoCuenta = tipoCuenta
        pass
        
    def depositarDinero(self, cantidadIngresada):
        if cantidadIngresada >= 0:
            self.saldo += cantidadIngresada
            print(f"La cantidad que usted ingreso es: {cantidadIngresada} al nombre del titular: {self.titular}. Su nuevo saldo es: {self.saldo}")
        else: 
            print("Ingrese una cantidad mayor a 0. Intentelo de nuevo")
    
    def retirarDinero(self, cantidad):
        if cantidad >= 0:
            self.saldo >= cantidad
            self.saldo -= cantidad
            print(f"La cantidad que usted retiro es: {cantidad} al nombre del titular: {self.titular}. Su nuevo saldo es: {self.saldo}")
        else:
            print("El saldo a retirar debe ser mayor a 0")
            
    def mostrarSaldo(self):
        print(f"TITULAR: {self.titular}")
        print(f"SALDO: {self.saldo}")
        print(f"TIPO DE CUENTA: {self.tipoCuenta}")
        
        
Cuenta = CuentaBancaria("Juan", 1000, "Ahorro")
Cuenta.depositarDinero(500)
Cuenta.retirarDinero(300)
Cuenta.mostrarSaldo()
        
        
