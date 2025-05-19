#Clase CuentaCorreo: email, contraseña (la contraseña debe tener al menos 6 caracteres)
class CuentaCorreo:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, caracteres):
        if len(caracteres) >= 6:
            self._password = caracteres
        else:
            raise ValueError("La contraseña debe de tener al menos 6 caracteres")
        
    @password.deleter
    def password(self):
        print("La contraseña ha sido eliminado correctamente")
        del self._password
        
x = CuentaCorreo("eliasfranco@gmail.com", "123456")
print(x.password)
x.password =  "123445678910Elias" # Modificamos la contraseña con setter
print(f"La nueva contraseña modificada es: {x.password}")
del x.password
        
            