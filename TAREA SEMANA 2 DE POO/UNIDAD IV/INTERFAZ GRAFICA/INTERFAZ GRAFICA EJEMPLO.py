import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entrada.get()
    if dato:
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_lista():
    lista.delete(0, tk.END)

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")
ventana.geometry("400x400")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Introduce un dato:")
etiqueta.pack(pady=5)

# Crear un campo de entrada
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Crear un botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="lightblue", fg="black")
boton_agregar.pack(pady=5)

# Crear una lista para mostrar los datos
titulo_lista = tk.Label(ventana, text="Lista de datos ingresados:")
titulo_lista.pack(pady=5)

lista = tk.Listbox(ventana)
lista.pack(pady=5)

# Crear un botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista, bg="lightcoral", fg="black")
boton_limpiar.pack(pady=5)

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir, bg="lightgray", fg="black")
boton_salir.pack(pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
