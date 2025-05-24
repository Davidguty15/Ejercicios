#Estructura de los diccionarios en python
# # Un diccionario es una colección desordenada, modificable e indexada de pares clave-valor.
# # Los diccionarios se definen utilizando llaves {} y los pares clave-valor se separan por comas.
# # Las claves deben ser únicas y pueden ser de cualquier tipo inmutable (números, cadenas, tuplas, etc.).
# # Los valores pueden ser de cualquier tipo y pueden repetirse.
#
# # Ejemplo de un diccionario simple
diccionario = {
    "nombre": "Juan",
    "edad": 30 ,
    "ciudad": "Madrid",
    1: "uno",
    True : "hola"}

print(diccionario)
# # Este código crea un diccionario llamado "diccionario" con tres pares clave-valor: "nombre", "edad" y "ciudad".

# # Imprime el diccionario completo.
# # Este código imprime el diccionario completo.
#
# # Accediendo a los valores del diccionario
# print(diccionario["nombre"])  # Imprime "Juan"
# print(diccionario["edad"])    # Imprime 30
# print(diccionario["ciudad"])  # Imprime "Madrid"
# # Este código accede a los valores del diccionario utilizando las claves correspondientes.
# # Este código imprime los valores asociados a las claves "nombre", "edad" y "ciudad".
#
# # Modificando valores en el diccionario
# diccionario["edad"] = 31
# print(diccionario)
# # Este código modifica el valor asociado a la clave "edad" en el diccionario.
# # Este código imprime el diccionario modificado.
#
# # Agregando un nuevo par clave-valor al diccionario
# diccionario["profesion"] = "Ingeniero"
# print(diccionario)
# # Este código agrega un nuevo par clave-valor al diccionario.
# # Este código imprime el diccionario modificado con la nueva clave "profesion".
#
# # Eliminando un par clave-valor del diccionario
# del diccionario["ciudad"]
# print(diccionario)
# # Este código elimina el par clave-valor asociado a la clave "ciudad" del diccionario.
# # Este código imprime el diccionario modificado sin la clave "ciudad".
#
# # Iterando sobre un diccionario
# for clave, valor in diccionario.items():
#     print(f"{clave}: {valor}")
# # Este código itera sobre cada par clave-valor del diccionario e imprime la clave y el valor.
# # Este código imprime cada clave y valor del diccionario.
#
# # Comprobando si una clave existe en el diccionario
# if "nombre" in diccionario:
#     print("La clave 'nombre' existe en el diccionario.")
# else:
#     print("La clave 'nombre' no existe en el diccionario.")
# # Este código comprueba si la clave "nombre" existe en el diccionario y muestra un mensaje correspondiente.
# # Este código imprime un mensaje indicando si la clave "nombre" existe o no en el diccionario.
#
# # Longitud del diccionario
print(len(diccionario))  # Imprime la cantidad de pares clave-valor en el diccionario
# # Este código imprime la longitud del diccionario, es decir, la cantidad de pares clave-valor que contiene.
# # Este código imprime la cantidad de pares clave-valor en el diccionario.
#
# # Limpiando el diccionario
# diccionario.clear()
# print(diccionario)  # Imprime un diccionario vacío
# # Este código limpia el diccionario, eliminando todos los pares clave-valor.
# # Este código imprime un diccionario vacío después de limpiar el diccionario original.

# # Ejemplo de uso de diccionarios en un programa simple
# # Programa que almacena información de estudiantes
# estudiantes = {
#     "Juan": {"edad": 20, "carrera": "Ingeniería"},
#     "María": {"edad": 22, "carrera": "Medicina"},
#     "Pedro": {"edad": 21, "carrera": "Arquitectura"}
# }
#
# # Imprime la información de cada estudiante
# for estudiante, info in estudiantes.items():
#     print(f"Estudiante: {estudiante}")
#     print(f"Edad: {info['edad']}")
#     print(f"Carrera: {info['carrera']}")
#     print()

# # Este código crea un diccionario llamado "estudiantes" que almacena información de varios estudiantes, incluyendo su edad y carrera.
# # Luego, itera sobre el diccionario e imprime la información de cada estudiante.
# # Este código imprime la información de cada estudiante, incluyendo su nombre, edad y carrera.

# # Ejemplo de uso de diccionarios en un programa más complejo
# # Programa que cuenta la frecuencia de palabras en un texto
# texto = "Hola mundo. Hola a todos. Bienvenidos al mundo de Python."
# palabras = texto.split()
# frecuencia = {}
#
# # Cuenta la frecuencia de cada palabra en el texto
# for palabra in palabras:
#     palabra = palabra.strip(".")
#     if palabra in frecuencia:
#         frecuencia[palabra] += 1
#     else:
#         frecuencia[palabra] = 1
#
# # Imprime la frecuencia de cada palabra
# for palabra, cuenta in frecuencia.items():
#     print(f"{palabra}: {cuenta}")
# # Este código cuenta la frecuencia de cada palabra en un texto dado y almacena los resultados en un diccionario.
# # Luego, itera sobre el diccionario e imprime la frecuencia de cada palabra.
# # Este código imprime la frecuencia de cada palabra en el texto, mostrando cuántas veces aparece cada una.

