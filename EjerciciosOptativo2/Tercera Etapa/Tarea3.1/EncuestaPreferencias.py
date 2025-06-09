#- Preguntar nombre (Entry)
#- Preguntar color favorito (OptionMenu: Rojo, Verde, Azul, Otro)
#- Preguntar lenguaje favorito (Listbox con: Python, Java, C++, JavaScript)
#- Botón “Enviar respuesta”
#- Mostrar en pantalla lo que eligió

import tkinter as tk

window = tk.Tk()
window.title("Encuesta de Preferencias")
window.geometry("400x350")

def mostrar():
    name = entrada.get()
    color = select.get()
    seleccion = listbox.curselection()
    lenguaje = listbox.get(seleccion[0]) if seleccion else "Ninguno"
    resultado.config(text=f"Nombre: {name} | Color Favorito: {color} | Lenguaje Favorito: {lenguaje}")

entrada = tk.Entry(window)
entrada.pack()

opcions = ["ROJO", "VERDE", "AZUL", "OTRO"]
select = tk.StringVar(value=opcions[0])
menu = tk.OptionMenu(window, select, *opcions)
menu.pack()

listbox = tk.Listbox(window)
listbox.insert(0, "Python")
listbox.insert(1, "Java")
listbox.insert(2, "C++")
listbox.insert(3, "JavaScript")
listbox.pack()

boton = tk.Button(window, text="Enviar respuesta", command=mostrar)
boton.pack()

resultado = tk.Label(window, text="")
resultado.pack()

window.mainloop()
