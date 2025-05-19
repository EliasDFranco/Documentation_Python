#Crear una clase Vehiculo que tenga marca, modelo y color, y un método describir.

class Vehiculo:
    def __init__(self, marca, modelo, color, year, tipoVehiculo):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._year = year
        self._tipoVehiculo = tipoVehiculo
    def describirAuto(self):
        return f"Vehículo de marca: {self._marca} | Modelo: {self._modelo} | Color: {self._color} | Año de lanzamiento: {self._year} | Tipo de vehiculo: {self._tipoVehiculo}"
        
print("\n") 
v1 = Vehiculo("Mercedes-Benz","Clase C - c200", "Negro", 2025, "Sédan")
print(v1.describirAuto())

print("\n") 
v2 = Vehiculo("Toyota","Funcargo", "Dorado", 2003, "Carguero")
print(v2.describirAuto())

print("\n") 
v3 = Vehiculo("BMW","X6", "Blanco", 2024, "SUV")
print(v3.describirAuto())


