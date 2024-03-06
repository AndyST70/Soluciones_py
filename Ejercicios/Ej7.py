#7. Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con
#descuento. El descuento lo hace con base a la clave; si la clave es 01 el descuento es del 10% y si
#la clave es 02 el descuento en del 20% (solo existen dos claves).

#! desarrollo del programa
#* imprimirmos el nombre, clave, precio original, precio_descuento
#? descuento va depender de la clave
#? clave : (1|2)
#? 1 : 10% | 2 : 20%
def main():
    print("PROGRAMA DE COMPRAS")
    flag1 = True #booleano TRUE|FALSE
    while flag1:
        print("==================MENU======================")
        print("1.Ingresar articulo")
        print("2. Salir")
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            print("Ingresa compra")
            articulo = input("Nombre del articulo: ")
            clave = int(input("Clave: "))
            precio = float(input("Precio: "))
            
            compra(articulo, clave, precio) # 4 parametros
        elif opc == 2:
            print("Saliendo del programa... ADIOS :D")
            flag1 = False
        else:
            print("Opcion no valida")
def compra(articulo, clave, precio): # 3 parametros
    #calculos para nuestras operaciones
    descuento = 0
    if clave == 1:
        descuento = precio * 0.10
    elif clave == 2 :
        descuento = precio * 0.20
    else:
        print("Clave no valida")
    #* imprimirmos el nombre, clave, precio original, precio_descuento
    preciofinal =  precio - descuento
    print("articulo: ", articulo, "precio original", precio, "Total:", preciofinal, "descuento Q", descuento)

if __name__ == ("__main__"):
    main()