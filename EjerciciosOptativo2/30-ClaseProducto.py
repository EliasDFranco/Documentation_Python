class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        pass
    
    def calcularCosto(self):
        calcularTotal = self.precio * self.cantidad
        print(f"El nombre del producto: {self.nombre}. Su precio es: {self.precio}. La cantidad es: {self.cantidad}")
        print(f"El costo total es: {calcularTotal}")
        
imprimir = Producto("pizza", 1.5, 10)
imprimir.calcularCosto()