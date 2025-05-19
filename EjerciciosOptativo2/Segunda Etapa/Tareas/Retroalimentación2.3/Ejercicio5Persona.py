# Usar herencia para modelar una clase Persona y una clase Empleado con atributos 
# adicionales

class Persona:
    def __init__(self, nombre, apellido, cedulaIdentidad):
        self._nombre = nombre
        self._apellido = apellido
        self._cedulaIdentidad = cedulaIdentidad
        
    def mostrarInfoPersona(self):
        return f"NOMBRE: {self._nombre} | Apellido: {self._apellido} | C.I : {self._cedulaIdentidad}"
    
class Empleado(Persona):
    def __init__(self, nombre, apellido, cedulaIdentidad, cargoOcupado, salario, edad, experienciaYears):
        super().__init__(nombre, apellido, cedulaIdentidad)
        self._cargoOcupado = cargoOcupado
        self._salario = salario
        self._edad = edad 
        self._experienciaYears = experienciaYears
        
    def mostrarInfoPersona(self):
        informacion =  super().mostrarInfoPersona()
        return f"{informacion} Cargo Ocupado: {self._cargoOcupado} | Salario: {self._salario} | Edad: {self._edad} | Años de Experiencia: {self._experienciaYears}"

c1 = Persona("Elias", "Franco Duarte", 6167356)
print(c1.mostrarInfoPersona())

c2 = Empleado("Ariel", "Franco Duarte", 245676, "Auxiliar Informático", 12000000, 21, 10)
print(c2.mostrarInfoPersona())

