
#! Ejercicio 3
list_numeros = []
def main():
    cont1 = 0 #positivos
    cont2 = 0 #negativos
    cont3 = 0 #neutrs
    print("Ingrese 20 numeros por favor")
    for indexar in range(20):
        numeros = int(input(": "))
        if numeros > 0:
            cont1 +=1
        elif numeros <0:
            cont2 +=1
        else:
            cont3 +=1
    print("mi numeros de conteos son los siguientes")
    print("+", cont1, "-", cont2, "N", cont3)

if __name__ == "__main__":
    main()