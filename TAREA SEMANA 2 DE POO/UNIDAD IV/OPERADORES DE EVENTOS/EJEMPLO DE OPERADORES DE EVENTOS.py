import tkinter as tk
from tkinter import messagebox

class GestorDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("500x450")

        # Lista para manejar las tareas
        self.tareas = []

        # Etiqueta de instrucciones
        self.instrucciones = tk.Label(root, text="Escribe una tarea y presiona Enter o el botón Agregar", font=("Arial", 12))
        self.instrucciones.pack(pady=(10, 0))

        # Campo de entrada de texto
        self.entrada_tarea = tk.Entry(root, font=("Arial", 14))
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.focus_set()

        # Lista visual de tareas
        self.lista_tareas = tk.Listbox(root, font=("Arial", 12), selectbackground="lightblue", height=10)
        self.lista_tareas.pack(pady=10, fill=tk.BOTH, expand=True)

        # Botones funcionales
        self.boton_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack(pady=5)

        self.boton_completar = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Vinculación de teclas
        root.bind("<Return>", self.tecla_enter)
        root.bind("<Escape>", self.salir_aplicacion)
        root.bind("<c>", self.tecla_completar)
        root.bind("<d>", self.tecla_eliminar)
        root.bind("<Delete>", self.tecla_eliminar)

        # Vinculación de eventos del mouse con la lista de tareas
        self.lista_tareas.bind("<Button-1>", self.clic_izquierdo)
        self.lista_tareas.bind("<Button-2>", self.clic_scroll)
        self.lista_tareas.bind("<Button-3>", self.clic_derecho)
        self.lista_tareas.bind("<Enter>", self.mouse_entrar)
        self.lista_tareas.bind("<Leave>", self.mouse_salir)

        # Etiqueta para mostrar el tipo de clic
        self.info_mouse = tk.Label(root, text="", font=("Arial", 10), fg="gray")
        self.info_mouse.pack(pady=5)

    def agregar_tarea(self):
        texto = self.entrada_tarea.get().strip()
        if texto:
            tarea_formateada = "[ ] " + texto
            self.lista_tareas.insert(tk.END, tarea_formateada)
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea = self.lista_tareas.get(indice)
            if tarea.startswith("[ ]"):
                nueva_tarea = tarea.replace("[ ]", "[✓]", 1)
            elif tarea.startswith("[✓]"):
                nueva_tarea = tarea.replace("[✓]", "[ ]", 1)
            else:
                nueva_tarea = tarea
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, nueva_tarea)
        else:
            messagebox.showinfo("Selecciona algo", "Debes seleccionar una tarea para marcarla.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.lista_tareas.delete(indice)
        else:
            messagebox.showinfo("Nada seleccionado", "Selecciona una tarea para eliminar.")

    def salir_aplicacion(self, event=None):
        self.root.quit()

    def tecla_enter(self, event):
        self.agregar_tarea()

    def tecla_completar(self, event):
        self.marcar_completada()

    def tecla_eliminar(self, event):
        self.eliminar_tarea()

    # Eventos del mouse inspirados en tu ejemplo B
    def clic_izquierdo(self, event):
        self.info_mouse.config(text="Clic izquierdo detectado en la lista.")

    def clic_derecho(self, event):
        self.info_mouse.config(text="Clic derecho detectado. ¡Puedes usarlo para consultar!")

    def clic_scroll(self, event):
        self.info_mouse.config(text="Clic de scroll detectado. No hace nada aún, pero se puede extender.")

    def mouse_entrar(self, event):
        self.lista_tareas.config(bg="lightyellow")

    def mouse_salir(self, event):
        self.lista_tareas.config(bg="white")
        self.info_mouse.config(text="")  # Limpiamos mensaje

# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorDeTareas(root)
    root.mainloop()
