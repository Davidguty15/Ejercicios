"""
Ejercicio 3: Validación de Acceso a un Sistema
Estás desarrollando un sistema de acceso que tiene diferentes niveles de seguridad.

Un usuario tiene acceso si su nombre de usuario es "admin" Y su contraseña es "password123".
O si el usuario tiene el rol de "supervisor" Y está conectado desde una "red_segura".
En cualquier otro caso, el acceso es denegado.
Instrucciones:

Pide al usuario que ingrese su nombre de usuario.
Pide al usuario que ingrese su contraseña.
Pide al usuario que ingrese su rol (por ejemplo, "usuario", "supervisor", "invitado").
Pide al usuario que ingrese la red desde la que está conectado (por ejemplo, "red_segura", "red_publica").
Usa una declaración if con and y or (y paréntesis para agrupar condiciones) para determinar si el acceso es concedido.
Imprime un mensaje indicando si el "Acceso concedido" o "Acceso denegado".
"""
# Solicitar al usuario que ingrese su nombre de usuario
usuario = input("Ingrese su nombre de usuario: ").strip()
# Solicitar al usuario que ingrese su contraseña
contrasena = input("Ingrese su contraseña: ").strip()
# Solicitar al usuario que ingrese su rol
rol = input("Ingrese su rol (usuario, supervisor, invitado): ").strip().lower()
# Solicitar al usuario que ingrese la red desde la que está conectado
red = input("Ingrese la red desde la que está conectado (red_segura, red_publica): ").strip().lower()
# Determinar si el acceso es concedido
condicion1 = (usuario == "admin" and contrasena == "password123")
condicion2 = (rol == "supervisor" and red == "red_segura")
if (condicion1) or (condicion2):
    acceso = "Acceso concedido"
else:
    acceso = "Acceso denegado"
# Imprimir el mensaje de acceso
print(acceso)


'''Forma 2 evaluando 2 condiciones por separado'''
# Solicitar al usuario que ingrese su nombre de usuario
# usuario = input("Ingrese su nombre de usuario: ").strip()
# # Solicitar al usuario que ingrese su contraseña
# contrasena = input("Ingrese su contraseña: ").strip()
# # Solicitar al usuario que ingrese su rol
# rol = input("Ingrese su rol (usuario, supervisor, invitado): ").strip().lower()
# # Solicitar al usuario que ingrese la red desde la que está conectado
# red = input("Ingrese la red desde la que está conectado (red_segura, red_publica): ").strip().lower()
# # Verificar si el usuario es admin con la contraseña correcta
# acceso_admin = usuario == "admin" and contrasena == "password123"
# # Verificar si el usuario es supervisor en una red segura
# acceso_supervisor = rol == "supervisor" and red == "red_segura"
# # Determinar si el acceso es concedido
# if acceso_admin or acceso_supervisor:
#     acceso = "Acceso concedido"
# else:
#     acceso = "Acceso denegado"
# # Imprimir el mensaje de acceso
# print(acceso)