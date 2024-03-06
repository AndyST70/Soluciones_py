#8. Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres
#camisas o más se aplica un descuento del 20% sobre el total de la compra y si son menos de tres
#camisas un descuento del 10%

#* total_pagar, cantidad_camisas, precio_camisa
def main():
    total_a_pagar = 0
    cantidad_camisas = 0
    precio_camisa = 0
    descuento = 0
    print("PROGRAMA DE COMPRAS")
    flag1 = True #booleano TRUE|FALSE
    while flag1:
        print("==================MENU======================")
        print("1. ingreso de camisas ")
        print("2. Salir")
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            print("Ingresa compra")
            print("Ingresa la cantidad de camisas")
            cantidad_camisas = int(input("Cantidad de camisas: "))
            precio_camisa = float(input("Precio por camisa: "))
            calculos(cantidad_camisas, precio_camisa)
        elif opc == 2:
            print("Saliendo del programa... ADIOS :D")
            flag1 = False
        else:
            print("Opcion no valida")

def calculos(cantidad_camisas, precio_camis):
    print("Calculando...")
    descuento = 0
    if cantidad_camisas >= 3:
        descuento = cantidad_camisas*(precio_camis * 0.20)
    else:
        descuento = cantidad_camisas*(precio_camis * 0.10)
    total_pagar = (cantidad_camisas * precio_camis) - descuento
    total = (cantidad_camisas*precio_camis)
    print("total",total ,"Total a pagar: Q", total_pagar, "Descuento: Q", descuento)


if __name__ == "__main__":
    print("EJRCICIO 8")
    main()