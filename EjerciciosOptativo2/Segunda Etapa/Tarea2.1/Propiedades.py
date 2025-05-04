# Practica con propiedades
class claseEjemplo:
    def __init__(self):
        self._atributo = valor
        
@property
    def atributo(self):
    """Getter: devuelve el valor atributo"""
    return self._atributo

@atributo.settetr
def atributo(self, nuevoValor):
    """Setter: modifica el valor del atributo"""
    if nuevoValor >= 0:
        self.atributo = nuevoValor
    else: 
        raise ValueError("El valor debe ser mayor o igual a 0")
    
@atributo.deleter
def atributo(self):
    """Deleter: elimina el atributo"""
    print("El atributo ha sido eliminado")
    del self._atributo