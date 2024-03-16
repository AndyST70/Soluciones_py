#26 Escriba un programa que permita leer un archivo secuencial, que contiene números del sistema
#decimal menores a 2000 separados por *. Entre un número y otro pueden aparecer separadores
#como espacios en blanco y tab.
#Los datos del archivo deben ser cargados a una matriz, posteriormente debe recorrer la matriz
#por filas y escribir en un nuevo archivo secuencial llamado romanos.txt, los números en su
#equivalente número romano, separados por “;”.
#Debe implementar dos contadores gestionados por su programa, de forma que al final del
#archivo muestre estos datos que representarán lo siguiente:
#● Número de líneas en el archivo de entrada
#● Dígitos en el archivo de entrada
#Su programa debe contener una función desarrollada por usted, que recibe como parámetro el
#número en el sistema decimal, y devuelve un string que representa el mismo número ya
#convertido a su correspondiente numeración en romano.
#El archivo datos1.txt tiene cuatro números enteros en cada línea:
#8 *525* 15* 20
#1550* 910 * 1995 * 5
#El archivo de salida romanos.txt debería mostrar lo siguiente:
#VIII; DXXV; XV; XX
#MDL; CMX; MCMXCV; V
#Número de líneas en el archivo de entrada: 2
#Dígitos en el archivo de entrada: 20


def main():
    print("Ejercicio 26")
    archivo_entrada = "datos2.txt"
    archivo_Salida = "romanos.txt"
    convertir_a_romano(archivo_entrada, archivo_Salida)
    lineas, digitos = contar(archivo_entrada)
    print(f"Numero de lineas en el archivo de entrada: {lineas}")
    print(f"Digitos en el archivo de entrada: {digitos}")

def contar(archivo):
    contador_lineas = 0
    contador_digitos = 0
    with open(archivo, 'r') as f:
        for linea in f:
            contador_lineas += 1
            for caracter in linea:
                if caracter.isdigit(): #estamos contando el dato
                    contador_digitos += 1
    return contador_lineas, contador_digitos


def convertir_a_romano(arch_entrada, arch_salida):
    with open(arch_entrada, "r", encoding="utf-8") as archivo:
        with open(arch_salida, "w", encoding="utf-8") as arc_salida:
            for i in archivo:
                numeros = i.strip().split("*")
                numeros_romanos = []
                for j in numeros:
                    if j != "":
                        numeros_romanos.append(romano(int(j)))
                arc_salida.write(";".join(numeros_romanos) + "\n")
                

def romano(numero):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    romano = ''
    for val, simbolo in valores:
        while numero >= val:
            romano += simbolo
            numero -= val
    return romano           

if __name__ == "__main__":
    main()