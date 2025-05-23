#Calculadora simple

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicación, división): ").lower()

if operacion == "suma":
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "resta":
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "multiplicación":
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "división":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida. Por favor, elige entre suma, resta, multiplicación o división.")