#pip install mysql-connect-python   
import mysql.connector

conexion = mysql.connector.connect(
    user='root',
    password='kr0954679692',
    host='localhost',
    database='usuario',
    port=3306  # Elimina las comillas alrededor de 3306
)

cursor  = conexion.cursor()

consulta = "INSERT INTO usuarios (nombre, apellido) VALUES (%s, %s)"

valor1 = "Carlos"
valor2 = "Moran"

datos_a_insertar = (valor1, valor2)
cursor.execute(consulta, datos_a_insertar)

# Confirmar la inserción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
