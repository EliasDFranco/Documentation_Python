class claseEjemplo:
    def __init__(self, valor):
        self._atributo = valor
    
    @property
    def atributo(self):
        """Getter: devuelve el valor del atributo"""
        return self._atributo

    @atributo.setter
    def atributo(self, nuevoValor):
        """Setter: modifica el valor del atributo"""
        if nuevoValor >= 0:
            self._atributo = nuevoValor  # Aquí debe asignarse a self._atributo, no a self.atributo
        else:
            raise ValueError("El valor debe ser mayor o igual a 0")
    
    @atributo.deleter
    def atributo(self):
        """Deleter: elimina el atributo"""
        print("El atributo ha sido eliminado")
        del self._atributo