class Calculadora:
    def __init__(self, n1 , n2):
        self.n1 = n1 
        self.n2 = n2
    
    def Suma(self):
        return self.n1 + self.n2
    
    def Resta(self):
        return self.n1 - self.n2
    
    def Multi(self):
        return self.n1 * self.n2
        
    def Divi(self):
        if self.n2 != 0:
            return self.n1  / self.n2
        else:
                print("El segundo número debe ser divisle y no puede ser 0")

def operaciones():  
    
    n1 = float(input("Ingresa un número: "))
    n2 = float(input("Ingresa otro número: "))
    
    print("Opciones de Operaciones: ")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISIÓN")
    
    calculador = Calculadora(n1, n2)
    operacion = input("Ingrese que operación quiere realizar: ")
    
    
    if operacion == "1":
        resultados = calculador.Suma()
        print(f"El resultado de la suma entre los números {n1} y {n2} es: {resultados}")
    elif operacion == "2":
        resultados = calculador.Resta()
        print(f"El resultado de la resta entre los números {n1} y {n2} es: {resultados}")
    elif operacion == "3":
        resultados = calculador.Multi()
        print(f"El resultado de la multiplicación entre los números {n1} y {n2} es: {resultados}")
    elif operacion == "4":
        resultados = calculador.Divi()
        print(f"El resultado de la división entre los números {n1} y {n2} es: {resultados}")
    else:
        print("No existe el número de operación que introduciste. Prueba de nuevo")

operaciones()    