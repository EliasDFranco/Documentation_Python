class Paquete:
    def __init__(self, nombrePaquete, destinatario, estado="Pendiente"):
        self._nombrePaquete = nombrePaquete
        self._destinatario = destinatario
        self._estado = estado
        
    def __str__(self):
        return f"Nombre del Paquete: {self._nombrePaquete} | Destinatario: {self._destinatario} | Estado del paquete: {self._estado}"
    
    @property
    def nombrePaquete(self):
        return self._nombrePaquete
    
    @property
    def destinatario(self):
        return self._destinatario
    
    @property 
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, nuevoEstado):
        self._estado = nuevoEstado
    
listaPaquetes = [
    Paquete("Elias", "San Lorenzo", estado = "En camino"),
    Paquete("Juan", "Villa Elisa", estado = "Engregado"),
    Paquete("María", "Fernando de la Mora", estado = "Cancelado"),
    Paquete("Ariel", "San Lorenzo", estado = "Entregado"),
    Paquete("Alexis", "Pedro Juan Caballero", estado = "En camino")
]

for paquete in listaPaquetes:
    if paquete.estado ==  "En camino":
        paquete._estado = "Entregado"
        
print("Estado de los paquetes actualizados")
for paquete in listaPaquetes:
    print(paquete)
        