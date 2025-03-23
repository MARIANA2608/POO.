import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Menú principal
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.archivo_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Salir", command=self.root.quit)

        # Frame para entrada de datos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Etiquetas y entradas
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.entry_fecha = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white',
                                     borderwidth=2)
        self.entry_fecha.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.entry_hora = tk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entry_descripcion = tk.Entry(self.frame_entrada)
        self.entry_descripcion.grid(row=2, column=1)

        # Botones
        self.boton_agregar = tk.Button(self.frame_entrada, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.grid(row=3, columnspan=2, pady=5)

        # Frame para lista de eventos
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Botón para eliminar eventos
        tk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(pady=5)

        # Botón para salir
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()
        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_fecha.set_date("")
            self.entry_hora.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar el evento?")
            if respuesta:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
