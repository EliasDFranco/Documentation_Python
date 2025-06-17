#Enunciado: Crear una interfaz que permita ingresar el nombre completo y el país de origen del usuario.
#Al hacer clic en el botón, mostrar en una etiqueta el mensaje:
#"¡Bienvenido, [nombre] de [país]!"
#Validar que ambos campos no estén vacíos.

import tkinter as tk

window = tk.Tk()
window.title("MENSAJE DE BIENVENIDA AL PAIS")
window.geometry("600x600")

labelNombre = tk.Label(window, text="Ingrese su nombre por favor!!")
labelNombre.pack()
entradaNombre = tk.Entry(window, font=("Times New Roman" , 15))
entradaNombre.insert(0, "")
entradaNombre.pack()

labelNacionalidad = tk.Label(window,  text="Ingrese su nacionalidad")
labelNacionalidad.pack()
entradaNacionalidad = tk.Entry(window, font=("Times New Roman", 15))
entradaNacionalidad.insert(0, "")
entradaNacionalidad.pack()

etiquetaResultado = tk.Label(window, text="")
etiquetaResultado.pack()

def mostrarBienvenidad():
    nombre = entradaNombre.get().strip()
    nacionalidad = entradaNacionalidad.get().strip()
    
    if nombre and nacionalidad and nombre != "Ingrese su nombre por favor!!" and nacionalidad != "Ingrese su nacionalidad":
        msj = f"Bienvenido {nombre} de {nacionalidad}"
        etiquetaResultado.config(text=msj)
    
    else:
        etiquetaResultado.config(text="Ingrese los valores correspondientes a cada campo, por favor!!", fg="red")
        
botonMostrarMensaje = tk.Button(text="LOS RESULTADOS: ", font=("Times New Roman", 14), command= mostrarBienvenidad)
botonMostrarMensaje.pack()

window.mainloop()