class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre 
        self._edad = edad
    
    @property
    def nombre(self):
        """Getter para el atributo nombre"""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevoNombre):
        """Setter para el atributo nombre"""
        if len(nuevoNombre) > 0:
            self._nombre = nuevoNombre
        else:
            raise ValueError("El nombre no puede estar vacío")
    
    @property
    def edad(self):
        """Getter para el atributo edad"""
        return self._edad
    
    @edad.setter
    def edad(self, nuevaEdad):
        """Setter para el atributo edad"""
        if nuevaEdad >= 0:
            self._edad = nuevaEdad
        else:
            raise ValueError("La edad no puede ser negativa")
    
    @edad.deleter
    def edad(self):
        """Deleter para el atributo edad"""
        print("El atributo 'edad' ha sido eliminado")
        del self._edad