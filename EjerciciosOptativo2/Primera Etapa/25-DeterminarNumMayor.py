nombre = input("Ingresar su nombre ")

n1 = float(input("Ingresa su 1er número"))
n2 = float(input("Ingresa su 2do número"))

if n1 > n2:
    mayorNum = n1
    
elif n1 < n2:
    mayorNum = n2
    
print(f"El numero mayor es: {mayorNum}")
    
