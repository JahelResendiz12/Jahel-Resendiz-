import sqlite3

# Conectar a la base de datos (si no existe, la crea)
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla (si no existe)
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    correo TEXT NOT NULL
)
''')

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Base de datos y tabla creadas con éxito.")

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Insertar datos
cursor.execute('''
INSERT INTO usuarios (nombre, edad, correo) 
VALUES (?, ?, ?)
''', ('Juan Pérez', 30, 'juan.perez@email.com'))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos insertados con éxito.")

# Conectar a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()

# Consultar todos los usuarios
cursor.execute('SELECT * FROM usuarios')

# Obtener los resultados
usuarios = cursor.fetchall()

# Mostrar los resultados
for usuario in usuarios:
    print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}, Correo: {usuario[3]}")

# Cerrar la conexión
conn.close()