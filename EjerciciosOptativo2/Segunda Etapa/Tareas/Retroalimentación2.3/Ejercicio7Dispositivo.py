class Dispositivo:
    def __init__(self, modeloCell, nvlBateria):
        self._modeloCell = modeloCell
        self._nvlBateria = nvlBateria
        
        
    @property
    def modeloCell(self):
        return self._modeloCell
    
    @property
    def nvlBateria(self):
        return self._nvlBateria
    
    @nvlBateria.setter
    def nvlBateria (self, valorBateria):
        if 0 <= valorBateria <= 100:
            self._nvlBateria = valorBateria
            print("EL nivel de bateria de su celular está perfecto")  
            
    def mostrarInfo(self):
        return f"Modelo del Celular: {self._modeloCell} | Nivel de Bateria: {self._nvlBateria} %"
            
c1 = Dispositivo("Iphone 11", 90)
print(c1.mostrarInfo())
            
            
c2 = Dispositivo("SAMSUNG A19", 20)
print(c2.mostrarInfo())