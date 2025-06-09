import tkinter as tk

def verificarProducto():
    recomendar = var.get()
    comment = cajaComentario.get("1.0", tk.END ).strip()
    nombre = entrynombre.get().strip()

    if recomendar == 1:
        etiquetaRecomendacion.config(text="No, no quiero recomendar el producto")
        textoRecomendacion = "No"
    else:
        etiquetaRecomendacion.config(text="Sí, sí quiero recomendar el producto")
        textoRecomendacion = "Sí"

    mostrarDatos = f"NOMBRE CLIENTE: {nombre}\nRECOMENDACIÓN: {textoRecomendacion}\nCOMENTARIO: {comment}"
    etiquetaResumen.config(text=mostrarDatos)

window = tk.Tk()
window.title("Encuesta de Satisfacción de producto")

var = tk.IntVar()
checkear = tk.Checkbutton(window, text="No recomiendo", variable=var)
checkear.pack()

entrynombre = tk.Entry(window, width=100)
entrynombre.insert(0, "Nombre del Cliente: ")
entrynombre.pack()

cajaComentario = tk.Text(window, height=10, width=100)
cajaComentario.pack()

botonRecomendar = tk.Button(window, text="Guardar Opinión", command=verificarProducto)
botonRecomendar.pack()

etiquetaRecomendacion = tk.Label(window, text="")
etiquetaRecomendacion.pack()

etiquetaResumen = tk.Label(window, text="", justify="left", wraplength=600)
etiquetaResumen.pack()

window.mainloop()