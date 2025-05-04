class Estudiante:
    def __init__(self, nombreAlumna, notas):
        self.nombreAlumna = nombreAlumna
        self.notas = notas
        pass
    
    def calcularNota(self):
        promedio = sum(self.notas) / len(self.notas) 
        if promedio >= 60:
            print(f"La alumna {self.nombreAlumna} ha aprobado")
            print("Estado: Aprobado")
        else:
            print(F"La alumna {self.nombreAlumna} no ha aprobado")
            print("Estado: DESAPROBADO")
            
    def calcularPromedio(self):
        promedio = sum(self.notas) / len(self.notas) 
        print(f"El promedio de la alumna: {self.nombreAlumna}. Es de: {promedio}")
        
datos = Estudiante("Ana",[70,80,65])
datos.calcularNota()
datos.calcularPromedio()


