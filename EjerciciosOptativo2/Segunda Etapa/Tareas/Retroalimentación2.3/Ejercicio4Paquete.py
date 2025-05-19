# . Programar una clase Paquete que calcule volumen y verifique si el envío es urgente.
class Paquete:
    def __init__(self, alto, largo, ancho, urgente= False):
        self._alto = alto
        self._largo = largo
        self._ancho = ancho
        self._urgente = urgente
        
    def volumen(self):
        return self.alto * self.largo * self.ancho
    
    @property
    def alto(self):
        return self._alto
    
    @property
    def ancho(self):
        return self._ancho
    
    @property
    def largo(self):
        return self._largo
    @property
    def urgenteOno(self):
        return self._urgente
    
    
    @urgenteOno.setter
    def urgenteOno(self, valor):
        if isinstance(valor, bool):
            self._urgente = valor
            print("El asunto es de Suma urgencia")
            
        else: 
            print("El valor no es urgente")
            
    def mostrarInfo(self):
        print(f"Paquete: {self.alto} de altura, {self.largo} de largor, {self.ancho} de anchura")
        print(f"El volumen del paquete es: {self.volumen()}")
        print(f"{'Si es urgente' if self.urgenteOno else 'No es urgente' }")
        
c = Paquete(100, 200, 123, urgente=True)
c.mostrarInfo()

c2 = Paquete(6,5,4)
c2.urgenteOno = True
c2.mostrarInfo()

c3 = Paquete(10,10,10)
c3.urgenteOno= False
c3.mostrarInfo()