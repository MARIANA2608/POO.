class ConexionBaseDeDatos:
    def __init__(self, nombre_bd):
        # Este es el constructor que se ejecuta cuando creamos una instancia de la clase.
        # Inicializa el nombre de la base de datos y establece que la conexión aún no ha sido realizada.
        self.nombre_bd = nombre_bd
        self.conexion = None
        print(f"¡Hola! Se está iniciando la conexión con la base de datos '{self.nombre_bd}'.")

    def conectar(self):
        # Método para simular la conexión a la base de datos.
        # Aquí cambiamos el estado de la conexión a 'True', lo que indica que ahora estamos conectados.
        if not self.conexion:
            self.conexion = True
            print(f"Conexión exitosa a '{self.nombre_bd}' realizada con éxito.")
        else:
            print(f"Ya estás conectado a '{self.nombre_bd}'.")

    def desconectar(self):
        # Método para simular el cierre de la conexión.
        # Si ya estamos conectados, se procede a desconectar la base de datos.
        if self.conexion:
            print(f"Desconectando de '{self.nombre_bd}'... ¡Hasta pronto!")
            self.conexion = False
        else:
            print("No hay ninguna conexión activa para desconectar.")

    def __del__(self):
        # Destructor llamado automáticamente cuando el objeto ya no está en uso.
        # Se asegura de que la conexión se cierre si aún está activa.
        if self.conexion:
            print(f"El objeto ha sido destruido. Se cierra la conexión a '{self.nombre_bd}'.")
            self.desconectar()
        else:
            print(f"El objeto ha sido destruido, pero no había ninguna conexión activa en '{self.nombre_bd}'.")


# Usando la clase en el código
conexion_bd = ConexionBaseDeDatos("MiBaseDeDatos")
conexion_bd.conectar()
conexion_bd.desconectar()
# Cuando el objeto 'conexion_bd' ya no se necesite, Python llamará automáticamente al destructor.
del conexion_bd
