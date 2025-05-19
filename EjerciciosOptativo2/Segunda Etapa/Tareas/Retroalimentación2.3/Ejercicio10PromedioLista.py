class Estudiante:
    def __init__(self, nombre, notas):
        self._nombre = nombre 
        self._notas = notas
        
    @property 
    def nombre(self):
        return self._nombre
    
    @property
    def notas(self):
        return self._notas
    
    
    @notas.setter
    def notas(self, notasNuevas):
        if all(1 <= nota <= 5 for nota in notasNuevas):
            self._notas = notasNuevas
            
        else:
            print("Las notas son del 1 al 5")

    @property      
    def promedio(self):
        return round(sum(self.notas) / len(self._notas), 2 )
    
    def mostrarResultados(self):
        return f"ALUMNO: {self._nombre} | NOTAS: {self._notas} | PROMEDIO: {self.promedio}"
    
    def __str__(self):
        return self.mostrarResultados()

c = Estudiante("Elias Franco", [2,3,4,5,5])
print(c)
print("\n")

c1 = Estudiante("José",[2,3,4,5,3])
print(c1)
print("\n")

c2 = Estudiante("Alexa", [2,3,2,3,2])
print(c2)
    
