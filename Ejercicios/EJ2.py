




list_numeros = []
list_data_1 = []
#EJERCICIO 2
def main():
    print("Ingrese 10 numeros por favor")
    for indexar in range(5):
        numeros = int(input("numeros, I : "))
        list_numeros.append(numeros)
        #FORMA1 
        if numeros > 0 or numeros == 0: 
            list_data_1.append(numeros)
        else:
            print("debe ser un numero positivo")
            
    #forma 2
    for i in list_numeros:
        if i > 0:
            print("numeros positivos son los siguiente", i)

    
    print("numeros", list_data_1)


if __name__ == "__main__":
    main()