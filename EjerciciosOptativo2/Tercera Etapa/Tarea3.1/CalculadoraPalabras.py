#Area de texto para ingresar frases (Text)
#- Botón “Contar palabras”
#- Mostrar en un Label cuántas palabras hay
#- Agregar un botón “Limpiar texto

import tkinter as tk

def mostrarTxt():
    boxContent = box.get("1.0", tk.END)
    etiqueta.config(text=boxContent)
    
def contarTxt():
    boxContent = box.get("1.0", tk.END)
    words = boxContent.split()
    etiquetaWords.config(text=f"Total de palabras es: {len(words)}")
    
def limpiarTxt():
    box.delete("1.0", tk.END)
    etiqueta.config(text="")
    etiquetaWords.config(text="")
    
window = tk.Tk()
window.title("Agreggue comentarios acerca de la última película de Martin Scorsese")

box = tk.Text(window, height=10, width=35)
box.pack()

botonMostrar = tk.Button(window, text="Mostrar el texto", command=mostrarTxt)
botonMostrar.pack()

botonContar = tk.Button(window, text="Contar las palabras", command=contarTxt)
botonContar.pack()

botonLimpiar = tk.Button(window, text="Limpiar el comentario", command=limpiarTxt )
botonLimpiar.pack()

etiqueta = tk.Label(window, text="")
etiqueta.pack()

etiquetaWords = tk.Label(window, text="")
etiquetaWords.pack()

window.mainloop()