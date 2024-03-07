#15. Un programa donde el usuario debe ingresar 1 número y mostrar el resultado de calcular el
#factorial del número ingresado.
#Ejemplo: 5 = 5*4*3*2*1 = 120



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Solicitar al usuario que ingrese un número
    numero = int(input("Ingrese un número entero positivo: "))

    # Verificar si el número es positivo
    if numero < 0:
        print("El número debe ser positivo.")
        return

    # Calcular el factorial del número ingresado
    resultado = factorial(numero)

    # Mostrar el resultado
    print(f"El factorial de {numero} es: {resultado}")

if __name__ == "__main__":
    main()
