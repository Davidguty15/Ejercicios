
#Estructura del while en python
#while True:
#   print("Hola")
#    break
# Este código imprime "Hola" indefinidamente.


# Este código no imprime nada porque la condición es falsa desde el principio.
#i = 0
#while i < 10:
#    print(i)
#    i = i+3
# Este código imprime el valor de i mientras sea menor que 10. Sin embargo, si i no se inicializa antes del bucle, se producirá un error de referencia.

# while i < 10:
#     print(i)
#     i += 1
# Este código imprime el valor de i mientras sea menor que 10 y lo incrementa en 1 en cada iteración. Si i no se inicializa antes del bucle, se producirá un error de referencia.

# Ejemplo de uso de while con una lista
'''numeros = [2, 4, 3, 28, 55]
i = 2
while i < len(numeros):
   print(numeros[i])
   i += 2
   '''
# Este código imprime cada número de la lista "numeros" utilizando un bucle while. La variable i se inicializa en 0 y se incrementa en cada iteración hasta que alcanza la longitud de la lista.

# Ejemplo de uso de while con una cadena
'''
cadena = "Hola"
i = 0
while i < len(cadena):
    print(cadena[i])
    i += 1
    '''
# Este código imprime cada letra de la cadena "Hola" utilizando un bucle while. La variable i se inicializa en 0 y se incrementa en cada iteración hasta que alcanza la longitud de la cadena.

#Ejemplo de uso de while con un diccionario
diccionario = {"a": 1, "b": 2, "c": 3, "gato":9}
i = 1
claves = list(diccionario.keys())
while i < len(diccionario):
    clave = claves[i]
    valor = diccionario[clave]
    print(f"{clave}: {valor}")
    i += 1
# Este código imprime cada clave y valor del diccionario "diccionario" utilizando un bucle while. La variable i se inicializa en 0 y se incrementa en cada iteración hasta que alcanza la longitud de la lista de claves.

# Ejemplo de uso de while aplicado a un programa simple
# Programa simple que suma los números del 1 al 10
#suma = 0
#i = 1
#while i <= 10:
#    suma += i
#print(f"La suma de los números del 1 al 10 es: {suma}")
# Este código es un ejemplo de cómo usar el bucle while en Python para realizar una tarea simple, como sumar los números del 1 al 10.

# Ejemplo de while con un programa mas complejo
# Programa que calcula la suma de los números pares del 1 al 20
#suma_pares = 0
#i = 1
#while i <= 20:
#    if i % 2 == 0:
#        suma_pares += i
#    i += 1
#print(f"La suma de los números pares del 1 al 20 es: {suma_pares}")
# Este código es un ejemplo de cómo usar el bucle while en Python para realizar una tarea más compleja, como sumar los números pares del 1 al 20.
# Ejemplo de uso de while con un programa que pide al usuario que ingrese números

