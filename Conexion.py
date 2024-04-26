import mysql.connector

class ConexionMySQL:
    def __init__(self, host, usuario, contraseña, base_datos):
        self.host = host
        self.usuario = usuario
        self.contraseña = contraseña
        self.base_datos = base_datos
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.contraseña,
                database=self.base_datos
            )
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos MySQL")
        except mysql.connector.Error as err:
            print(f"No se pudo conectar a la base de datos MySQL: {err}")

    def desconectar(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")
