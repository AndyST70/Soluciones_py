#15. Un programa donde el usuario debe ingresar 1 número y mostrar el resultado de calcular el
#factorial del número ingresado.
#Ejemplo: 5 = 5*4*3*2*1 = 120


#pseudocode
#Función factorial(n):
#    Si n es igual a 0:
#        Devolver 1
#    Sino:
#        Devolver n * factorial(n - 1)

# n * factorial (n-1)



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


#Función principal():
#    Solicitar al usuario que ingrese un número entero positivo
#    Leer el número ingresado y almacenarlo en la variable numero

#    Si numero es menor que 0:
#        Mostrar "El número debe ser positivo."
#        Detener la ejecución del programa

#    Calcular el factorial del número ingresado llamando a la función factorial(numero) y almacenar el resultado en la variable resultado

#    Mostrar el resultado


def main():
    print("Factorial de un número")
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print("El número debe ser positivo.")
        return
    resultado = factorial(numero)
    print (f"El factorial de {numero} es {resultado}")

if __name__ == "__main__":
    main()