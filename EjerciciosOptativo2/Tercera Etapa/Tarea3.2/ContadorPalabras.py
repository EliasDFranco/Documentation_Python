import tkinter as tk

def contarTexto():
    boxContent = box.get("1.0", tk.END)
    words = boxContent.split()
    etiquetaWords.config(text=f"Total de palabras es: {len(words)}")

window = tk.Tk()
window.title("Agregue un texto por favor!!!")

box = tk.Text(window, height=10, width=35)
box.pack()

botonContar = tk.Button(window, text="Contar las palabras", command=contarTexto)
botonContar.pack()

e = tk.Label(window, text="")
e.pack()

etiquetaWords = tk.Label(window, text="")
etiquetaWords.pack()
window = tk.Tk()
window.title("CONTADOR DE PALABRAS")
window.geometry("1000x1000")

window.mainloop()