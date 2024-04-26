from Conexion import ConexionMySQL

# start the conecction
conexionMSQL = ConexionMySQL("192.168.100.100", "kelunie", "culep1711", "proyecto")
conexionMSQL.conectar()

PJ = "3-101-237976"
fecVen ="2025-05-01"
Distr = "Orotina Centro"
Ubi = "Orotina"
tel = 89477290
dirNom = "Dylan Recio"
dirEmail = "Drecio@email.com"

consulta = "INSERT INTO Juntas (PJ, fechVen, distri, ubicacion, telefono, dirNom, dirEmail) VALUES (%s, %s, %s, %s, %s, %s, %s)"
datos = (PJ, fecVen, Distr, Ubi, tel, dirNom, dirEmail)

# Crear un cursor para ejecutar la consulta
cursor = conexionMSQL.conexion.cursor()

try:
    # Ejecutar la consulta SQL
    cursor.execute(consulta, datos)

    # Confirmar los cambios
    conexionMSQL.conexion.commit()

    print("Datos insertados correctamente en la tabla Juntas.")
except Exception as e:
    print(f"Error al insertar datos: {e}")
    # Deshacer la transacción en caso de error
    conexionMSQL.conexion.rollback()

# Cerrar el cursor y la conexión
cursor.close()
conexionMSQL.desconectar()