import tkinter as tk 

window = tk.Tk()
window.title("CONVERTIDOR DE METROS A PIES")
window.geometry("600x600")

labelEntradaMts = tk.Label(window, text="Ingrese los metros")
labelEntradaMts.pack()
entradaMts = tk.Entry(window, text="")
entradaMts.pack()

etiquetaResultado = tk.Label(window, text="")
etiquetaResultado.pack()

def convertidorMTSaPies():
    mts = entradaMts.get()
    try:
        mts = float(mts)
        pies = mts * 3.28084
        etiquetaResultado.config(text=f"{mts} metros = {pies:.2f} pies")
    except ValueError:
        etiquetaResultado.config(text="Ingrese digitos válidos")

botonCalcular = tk.Button(window, text="Calcular conversión", command=convertidorMTSaPies)
botonCalcular.pack()
window.mainloop()