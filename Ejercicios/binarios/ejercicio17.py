def main():
    print("PROGRAMA DE BINARIOS")
    flag1 = True #booleano TRUE|FALSE
    while flag1:
        print("==================MENU======================")
        print("1. ingreso de numero binario ")
        print("2. ingreso de decimal ")
        print("3. Salir")
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            binario = input("Ingrese el numero binario: ")
            a = binario_decimal(binario)
            print(f"El numero decimal es: {a}")
        elif opc == 2:
            decimal = int(input("Ingresa el decimal "))  
            a = decimal_binario(decimal)
            print(f"El numero binario es: {a}")
        elif opc == 3:
            print("Saliendo del programa... ADIOS :D")
            flag1 = False
        else:
            print("Opcion no valida")


def binario_decimal(binario):
    decimal = 0
    potencia = 0
    for i in reversed(binario):
        if i == "1":
            decimal += 2 ** potencia
        potencia += 1
    return decimal


def decimal_binario(decimal):
    bin_arts = ""
    while decimal > 0:
        residuo = decimal % 2
        bin_arts = str(residuo) + bin_arts
        decimal //= 2
    return bin_arts


if __name__ == "__main__":
    main()
