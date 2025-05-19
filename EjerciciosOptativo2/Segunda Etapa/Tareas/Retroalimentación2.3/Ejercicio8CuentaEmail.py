class CuentaCorreo:
    def __init__(self, correo_electronico, contrasena):
        self._correo_electronico = correo_electronico
        self._contrasena = contrasena
        
    @property
    def contrasena(self):
        return self._contrasena
    
    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        if len(nueva_contrasena) >= 6:
            self._contrasena = nueva_contrasena
        else:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        
    @contrasena.deleter
    def contrasena(self):
        print("La contraseña ha sido eliminada correctamente")
        del self._contrasena

cuenta = CuentaCorreo("eliasfranco@gmail.com", "123456")
print(cuenta.contrasena)

cuenta.contrasena = "123445678910Elias"
print(f"La nueva contraseña modificada es: {cuenta.contrasena}")

del cuenta.contrasena
