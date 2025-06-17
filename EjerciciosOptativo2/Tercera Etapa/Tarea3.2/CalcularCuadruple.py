
import tkinter as tk

def calcular4():
    valor = entradaDatos.get()
    if valor.isdigit():
        result = int(valor) * 4
        etiquetaResultado.config(text=f"El valor cuadruple del numero ingresado es: {result}")
    else:
        etiquetaResultado.config(text="Usted ha ingresado un caracter no válido, ingrese un número!")
    

window = tk.Tk()
window.title("CALCULADORA CUADRUPLE")
window.geometry("600x600")

labelDatos = tk.Label(window, text="Ingrese un digito por favor!")
labelDatos.pack()
entradaDatos = tk.Entry(window, font=("Times New Roman ", 14))
entradaDatos.insert(0, "")
entradaDatos.pack()

etiquetaResultado = tk.Label(window, text="", font=("Times New Roman ", 14))
etiquetaResultado.pack()

botonCalcular = tk.Button(window, text="CALCULAR CUADRUPLE DEL DIGITO", font=("Times New Roman ", 13), command=calcular4)  
botonCalcular.pack()
window.mainloop()