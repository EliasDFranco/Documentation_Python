class Estudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        
    @property
    def promedio(self):
        return self._promedio
    
    @promedio.setter
    def promedio(self, promedioIngresado):
        if 1 <= promedioIngresado <= 5:
            self._promedio = promedioIngresado
        else: 
            raise ValueError("El promedio debe de ser un número de 1 entre 5. ")
    
    @promedio.deleter
    def promedio(self):
        print("El promedio ha sido eliminado.")
        del self._promedio 
        
x = Estudiante("Elias", 1) 
print(x.promedio)
x.promedio = 3
print(x.promedio)
del x.promedio      
        