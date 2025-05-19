#Crear una clase Estudiante con promedio y determinar si aprueba (>= 3).

class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, valoresNotas):
        if valoresNotas >= 3:
            self._nota = valoresNotas
            print("El promedio es mayor o igual a 3, usted ha aprobado")
        else:
            print("Usted no ha aprobado debe de tener un promedio de 3 para poder aprobar")
            
    def mostrarResultado(self):
        print(f"Estudiante: {self._nombre}, Promedio: {self._nota}")
        
c = Estudiante("Elias Franco Duarte", 5)

c.mostrarResultado()

c.nota = 2
print(f"La nota modificada es: {c.nota}")
c.mostrarResultado()



        