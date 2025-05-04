saldoUsuario = 10000

monto = int(input("Ingrese un monto para retirar del Cajero Auomático: "))

if monto > 0:
    if monto <= saldoUsuario:
        saldoUsuario -= monto
        print(f" Su saldo es {saldoUsuario }.  Puede retirar el monto deseado {monto}")
    else: 
        print(f" Su saldo es {saldoUsuario }.  No retirar el monto deseado {monto}")
        print(f" Puede retirar hasta {saldoUsuario}.")
else: 
    print(f"El monto tiene que ser mayor a 0")
