#25. Escriba un programa que permita sumar por fila y columna los números almacenados en un
#archivo de texto.
#El archivo datos1.txt tiene tres números enteros en cada línea:
#45 12 98
#1 12 65
#7 15 76
#54 23 1
#65 2 84
#Escriba la función sumar por línea que devuelve una lista con las sumas de todas las líneas del
#archivo separadas por coma (155, 78, 98, 78, 151).
#Escriba la función sumar por columna que devuelve una lista con las sumas de todas las tres
#columnas del archivo separadas por coma (172, 64, 324)


def main():
    print("Ejercicio 25")
    archivo = "datos1.txt"
    data = lectura(archivo)
    #Suma por filas
    suma_x_filas = sum_filas (data)
    print("suma por filas", suma_x_filas)
    #Suma por columnas
    suma_x_columnas  = sum_columnas(data)
    print("suma por columnas", suma_x_columnas)

def lectura(data):
    list_numeros = []
    try:
        with open(data, "r") as archivo:
            for y in archivo:
                fila = []
                for x in y.split(";"): #! separa por espacios, separa por ;, separa por ,
                    fila.append(int(x))
                list_numeros.append(fila)
        return list_numeros
    


    except Exception as e:
        print("Error: ", e)
def sum_filas(data):
    suma = []
    for x in data:
        var_suma = sum(x) #dat1+dat2+dat3
        suma.append(var_suma)
    return suma
def sum_columnas(data):
    suma_columnas = len(data[0])
    suma = [0]*suma_columnas
    for x in data:
        for y in range(suma_columnas):
            suma[y] += x[y]
    return suma
if __name__ == "__main__":
    main()