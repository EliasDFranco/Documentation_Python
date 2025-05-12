class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, nuevoPrecio):
        if nuevoPrecio > 0:
            self._precio = nuevoPrecio
            
        else: 
            raise ValueError("El precio debe de ser mayor a 0.")
        
    @precio.deleter
    def precio(self):
        print("El precio ha sido eliminado correctamente")
        del self._precio
        
x = Producto("Galleta", 20)
print(x.precio)
x.precio = 30
print(x.precio)
del x.precio 