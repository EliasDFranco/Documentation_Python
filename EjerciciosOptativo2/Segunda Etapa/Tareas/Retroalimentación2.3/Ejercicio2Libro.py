# 2. Escribir una clase Libro con propiedades validadas:
# el precio debe ser mayor a 5000 Gs

class Libro:
    def __init__(self, precio, nombreLibro, autor) :
        self._precio = precio
        self._nombreLibro = nombreLibro
        self._autor = autor
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valorLibro):
        if valorLibro > 5000:
            self._precio = valorLibro
            print(f"El precio del libro es {valorLibro} Gs")
        else: 
            print("El precio del libro debe  de ser mayor a 5000 Gs. intente de nuevo!!")
        
    @property
    def nombreLibro(self):
        return self._nombreLibro
    
    @property
    def autor(self):
        return self._autor
    
    def mostrarDatos(self):
        print(f"Nombre del libro: {self._nombreLibro} | Autor: {self._autor} | Precio: {self._precio}")
    
c = Libro(10000, "El diario de Anna Frank", "Anna Frank")
c.mostrarDatos()

c.precio = 4000



    
    

