#5. Escriba un programa sea capaz de sumar sólo los números impares que se encuentran entre 1 y
#80

def main():
    cont_suma = 0
    print("Numeros impares")
    for i in range(81):
        if (i%2 != 0):
            # != diferente
            # == igual
            # > mayor
            # < menor
            # >= mayor o igual
            # <= menor o igual 
            print("i: ", i)
            cont_suma += i   
    print("La suma de los numeros impares es: ", cont_suma)

if __name__ == "__main__":
    print("EJERCICIO 5")
    main()