#comentario
def main():
    #print(type(num1),"data")
    #! declaramos nuestros numeros
    num1= int(input("ingrese un numero:"))
    num2= int(input("ingrese un numero:"))
    print("entro")

    if num1 == num2:
        r = num1 * num2
    elif num1 > num2:   
        r = num1 - num2
    else:
        r= num1 + num2
    #print(num1),"data")
    #print("resultado:", r)
    print("resultado", r)
if __name__ == "__main__":
    print("EJERCICIO1")
    main()
