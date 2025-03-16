import tkinter as tk
from tkinter import messagebox

def insertar_dato():
    """Agrega el contenido del campo de texto a la lista."""
    contenido = campo_texto.get().strip()
    if contenido:
        lista_datos.insert(tk.END, contenido)
        campo_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Debe ingresar algún dato antes de añadirlo.")

def borrar_lista():
    """Elimina todos los elementos de la lista."""
    lista_datos.delete(0, tk.END)

def borrar_seleccionado():
    """Elimina el elemento seleccionado en la lista."""
    seleccion = lista_datos.curselection()
    if seleccion:
        lista_datos.delete(seleccion)
    else:
        messagebox.showwarning("Aviso", "Seleccione un elemento para eliminar.")

def salir():
    """Cierra la aplicación."""
    ventana.quit()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")
ventana.geometry("420x320")

# Centrar la ventana en la pantalla
ancho_ventana = 420
alto_ventana = 320
posicion_x = int((ventana.winfo_screenwidth() / 2) - (ancho_ventana / 2))
posicion_y = int((ventana.winfo_screenheight() / 2) - (alto_ventana / 2))
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

# Barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Borrar Todo", command=borrar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Etiqueta descriptiva
etiqueta = tk.Label(ventana, text="Ingrese información:")
etiqueta.pack(pady=5)

# Campo de entrada
campo_texto = tk.Entry(ventana)
campo_texto.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Añadir", command=insertar_dato)
boton_agregar.pack(pady=5)

# Lista donde se visualizarán los datos
lista_datos = tk.Listbox(ventana)
lista_datos.pack(pady=5, fill=tk.BOTH, expand=True)

# Botones para eliminar datos
boton_eliminar = tk.Button(ventana, text="Eliminar Seleccionado", command=borrar_seleccionado)
boton_eliminar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Borrar Todo", command=borrar_lista)
boton_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()

