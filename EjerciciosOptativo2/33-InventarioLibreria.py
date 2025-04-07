class Libros:
    def __init__(self, titulo, autor, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        
    def __str__(self):
        return f"TITULO: {self.titulo}. AUTOR: {self.autor}. CANTIDAD: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.Libros = []

    def agregarLibros(self, libro):
        self.Libros.append(libro)
        
    def verLibros(self):
        print("Inventario de Libros")
        for libro in self.Libros:
            print(libro)
            
    def calcularConsulta(self, titulo):
        for libro in self.Libros:
            if libro.titulo == titulo:
                print(f"El libro por titulo {libro.titulo}. Tiene una cantidad de {libro.cantidad}")
                return
        print(f"El libro {titulo} no esta en el inventario")
                
                
datos1 = Libros("1984", "George Orwell", 5)
datos2 = Libros("El Quijote", "Miguel de Cervantes", 3)
            
            
inventario = Inventario()
inventario.agregarLibros(datos1)
inventario.agregarLibros(datos2)

inventario.verLibros()
inventario.calcularConsulta("1984")
inventario.calcularConsulta("TRUENO ENTRE LAS HOJAS")