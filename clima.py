'''
Ejercicio 2: Determinación del Tipo de Día
Vas a crear un programa que clasifique un día según su clima y la hora del día.

Si el clima es "soleado" Y la hora está entre las 9 y las 18 (inclusive), es un "Día perfecto para actividades al aire libre".
Si el clima es "lluvioso" O la temperatura es menor a 10 grados Celsius, es un "Día para quedarse en casa con una buena película".
En cualquier otro caso, es un "Día normal".
Instrucciones:

Pide al usuario que ingrese el clima actual (por ejemplo, "soleado", "nublado", "lluvioso").
Pide al usuario que ingrese la hora actual en formato de 24 horas (un número entero, por ejemplo, 14 para las 2 PM).
Pide al usuario que ingrese la temperatura actual (un número entero o flotante).
Usa declaraciones if, elif, else con and y or para clasificar el día.
Imprime el mensaje correspondiente al tipo de día.
'''

# Solicitar al usuario que ingrese el clima actual
clima = input("Ingrese el clima actual (soleado, nublado, lluvioso): ").strip().lower()
# Solicitar al usuario que ingrese la hora actual en formato de 24 horas
hora = int(input("Ingrese la hora actual (0-23): "))
# Solicitar al usuario que ingrese la temperatura actual
temperatura = int(input("Ingrese la temperatura actual en grados Celsius: "))
# Clasificar el día según las condiciones ingresadas
if clima == "soleado" and 9 <= hora <= 18:
    tipo_dia = "Día perfecto"
elif clima == "lluvioso" or temperatura < 10:
    tipo_dia = "Día nublado"
else:
    tipo_dia = "Día normal"
# Imprimir el mensaje correspondiente al tipo de día
print(tipo_dia)  