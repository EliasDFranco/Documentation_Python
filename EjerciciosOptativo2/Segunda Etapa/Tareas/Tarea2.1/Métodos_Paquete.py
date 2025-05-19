#Ejemplo 2.1.2
# Creando una clase para paquete
class Paquete:
    def __init__(self, idPaquete, descripcion, peso, largo, ancho, alto, destino):
        self.idPaquete = idPaquete
        self.descripcion = descripcion
        self.peso = peso
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.destino = destino
        
        self.estado = "Pendiente"
        self.fechaCreacion = "2025-01-15"
        self.fechaEntregaEstimada = None
        
    def calcularVolumen (self):
        """ Calcula el volumen del paquete"""
        return self.largo * self.ancho * self.alto
        
    def calcularCostoEnvio(self, tarifa_x_Kl, tarifa_x_Volumen):
        """Calcula el costo de envio basado en peso y volumen"""
        costoPeso = self.peso * tarifa_x_Kl
        volumen = self.calcularVolumen()
        costoVolumen = volumen * tarifa_x_Volumen
        return max(costoPeso, costoVolumen)
        
    def actualizarEstado(self, nuevoEstado):
        """Actualiza el estado del paquete"""
        self.estado = nuevoEstado 
            
    def mostrarInformación(self):
        """Muestra los detalles del paquetes """
        return f"""
        ID: {self.idPaquete}
        Descripcion: {self.descripcion}
        Peso: {self.peso} kg
        Dimensiones: {self.largo}x{self.ancho}x{self.alto} cm
        Destino: {self.destino}
        Estado:{self.estado}
        Fecha de creación: {self.fechaCreacion}
        Fecha estimada de entrega: {self.fechaEntregaEstimada or 'No disponible el paquete'}
        """
#Creamos el paquete
paquete1 = Paquete("PKG0001", "Ropa deportiva",  2.5, 30,20,10, "San Lorenzo")

# Calcular el costo de envío
costoEnvio = paquete1.calcularCostoEnvio(tarifa_x_Kl=10, tarifa_x_Volumen=0)
print(f"Costo de envio {costoEnvio:2f} GS")

#Actualizar el estado del paquete
paquete1.actualizarEstado("En tránsito")

#Mostrar información del paquete
print(paquete1.mostrarInformación())