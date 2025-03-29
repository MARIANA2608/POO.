import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk


class ListaTareasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tareas")
        self.master.geometry("500x400")

        # Etiqueta y campo de entrada para nuevas tareas
        self.label_tarea = tk.Label(master, text="Nueva Tarea:")
        self.label_tarea.pack(pady=5)

        self.entrada_tarea = tk.Entry(master, width=50)
        self.entrada_tarea.pack(pady=5)
        self.entrada_tarea.bind("<Return>", self.agregar_tarea)

        # Botones
        self.boton_agregar = tk.Button(master, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = tk.Button(master, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista de tareas con Treeview
        self.treeview = ttk.Treeview(master, columns=('Tarea'), show='headings')
        self.treeview.heading('Tarea', text='Lista de Tareas')
        self.treeview.pack(pady=10, fill=tk.BOTH, expand=True)

        # Vincular eventos adicionales
        self.treeview.bind("<Double-1>", self.marcar_completada)
        self.master.bind("<Escape>", self.cerrar_aplicacion)
        self.master.bind("<z>", self.agregar_tarea)
        self.master.bind("<q>", self.marcar_completada)
        self.master.bind("<x>", self.eliminar_tarea)

    def agregar_tarea(self, event=None):
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.treeview.insert('', tk.END, values=(tarea,))
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar una tarea")

    def marcar_completada(self, event=None):
        seleccion = self.treeview.selection()
        if seleccion:
            for item in seleccion:
                tarea = self.treeview.item(item, "values")[0]
                self.treeview.item(item, values=(f"[✔] {tarea}",))
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada")

    def eliminar_tarea(self, event=None):
        seleccion = self.treeview.selection()
        if seleccion:
            for item in seleccion:
                self.treeview.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")

    def cerrar_aplicacion(self, event=None):
        messagebox.showinfo("Cerrar Aplicación", "Saliendo de la aplicación.")
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
