#Clase Dispositivo: modelo, nivel de batería (0 a 100%)
class Dispositivo: 
    def __init__(self, modelo, nivelBateria):
        self._modelo = modelo
        self._nivelBateria = nivelBateria
        
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def nivelBateria(self):
        return self._nivelBateria
    
    @modelo.setter
    def modelo(self, nuevoModelo):
        if len(nuevoModelo) > 12:
            self._modelo = nuevoModelo
            print("El modelo ha sido modificado correctamente")
        
    @nivelBateria.setter
    def nivelBateria(self, nuevoPorcentaje):
        if 0 <= nuevoPorcentaje <= 100:
            self._nivelBateria = nuevoPorcentaje
            print("El porcentaje de su batería está perfecto")
        
    @modelo.deleter
    def modelo(self):
        print("El modelo ha sido eliminado correctamente.")
        del self._modelo
        
x = Dispositivo("SAMSUNG GALAXY A24", 70)
print(f"El modelo del dispositivo es: {x._modelo}")
print(f"El nivel de batería del dispositivo es: {x._nivelBateria}")

x._modelo = "Iphone 13 Pro Max"
x._nivelBateria = 30
print(f"El modelo del dispositivo modificado es: {x._modelo}")
print(f"El nivel de batería del dispositivo modificado es: {x._nivelBateria}")

del x.modelo