import tkinter as tk

def procesar():
    nombre = entrada_nombre.get()
    texto_multilinea = texto.get("1.0", "end-1c")
    acepta = var_check.get()
    color = seleccion_color.get()
    lenguajes = lista_lenguajes.curselection()
    
    ventana.config(bg=color.lower())

    mensaje = f"Hola {nombre}!\n"
    mensaje += f"Mensaje: {texto_multilinea}\n"
    mensaje += f"Aceptó términos: {'Sí' if acepta else 'No'}\n"
    mensaje += f"Color elegido: {color}\n"
    if lenguajes:
        lenguaje_seleccionado = lista_lenguajes.get(lenguajes[0])
        mensaje += f"Lenguaje seleccionado: {lenguaje_seleccionado}\n"
    else:
        mensaje += "Lenguaje seleccionado: Ninguno\n"
        
    resultado.config(text=mensaje)

ventana = tk.Tk()
ventana.title("Interfaz completa")

tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Comentario:").pack()
texto = tk.Text(ventana, height=3, width=40)
texto.pack()

var_check = tk.IntVar()
check = tk.Checkbutton(ventana, text="Acepto los términos", variable=var_check)
check.pack()

tk.Label(ventana, text="Elige un color:").pack()
opciones = ["red", "green", "blue"]
seleccion_color = tk.StringVar(value=opciones[0])
menu = tk.OptionMenu(ventana, seleccion_color, *opciones)
menu.pack()

tk.Label(ventana, text="Lenguajes:").pack()
lista_lenguajes = tk.Listbox(ventana, height=3)
for i, lenguaje in enumerate(["Python", "Java", "C++"]):
    lista_lenguajes.insert(i, lenguaje)
lista_lenguajes.pack()

boton = tk.Button(ventana, text="Procesar", command=procesar)
boton.pack()

botonSalir = tk.Button(ventana, text="Salir del programa", command=ventana.destroy, bg="red", fg="whitesmoke")
botonSalir.pack()

resultado = tk.Label(ventana, text="", justify="left")
resultado.pack()

ventana.mainloop()
