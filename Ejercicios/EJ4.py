#Ejercicio 4

def main():
    cont_suma = 0
    print("Numeros pares")
    for i in range(101):
        if (i%2 == 0):
            cont_suma += i   
            print(i)
    print("La suma de los numeros pares es: ", cont_suma)

if __name__ == "__main__":
    main()
    #! ejercicio
    #? En este código estamos trabajando una suma
