#14. Elabore un programa en donde el usuario ingrese un número, y posteriormente muestre en
#pantalla la cantidad correspondiente de billetes en la que puede completarse ese monto. Debe
#utilizar los billetes empezando de la denominación mayor a la menor. Únicamente puede utilizar
#billetes de la siguiente denominación:
#• Q.50.00
#• Q.20.00
#• Q.10.00
#• Q.5.00
#• Q.1.00


#* Unidades / decenas
#* Variables list_dinero = [50, 20, 10, 5, 1], billetes = [], dinero = 0 vamos a ingresar a la maquina

def main():
    dinero_ingresado = int(input("Ingrese la cantidad de dinero: "))
    resultado = calculos(dinero_ingresado) #LISTA DE BILLETES [50:16, 20:2, 10:0, 5:1, 1:1 ]
    for i in range(len(resultado)):
        print("Billetes de ", resultado[i], " de ", [50, 20, 10, 5, 1][i])
    
def calculos(dinero):
    print("Dinero ingresado: ", dinero)
    list_dinero = [50, 20, 10, 5, 1]
    billetes = []
    for i in list_dinero:
        billetes.append(dinero // i)
        dinero = dinero % i

    return billetes

if __name__ == "__main__":
    main()