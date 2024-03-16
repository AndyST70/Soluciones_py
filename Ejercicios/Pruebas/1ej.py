#Desarrolle un programa que permita procesar el siguiente texto en un archivo de
#acceso secuencial que se el siguiente : 
#! El éxito radica en repetir 100 veces
#! de ser posible una situación y aún
#! 20veces mas para alcanzar 10 probabilidades
#! o al menos5 de ellas para logrr lo
#! que nos hemos propuesto
#El programa debe estar en capacidad de abrir el archivo para su lectura y extraer las
#cantidades numéricas de cada línea del archivo. Posteriormente cada cantidad extraída
#se debe presentar en un reporte de la siguiente manera:
#Línea del archivo – número obtenido – su equivalente en binario
#1 100 1100100
#3 20, 10 10100, 1010
#4 5 101
#? La forma de presentar el reporte puede quedar a discreción del
#? programador, solo se pide como requisito que sea en un objeto que
#? permita mostrar dicho reporte.

#cantidad numerica de cada linea
#extraer la info : linea archivo, numero obtenido, su equivalente en binario
#presentar el reporte
def main():

    try:
        with open("a1.txt", "r", encoding = "utf-8") as archivo:
            #? La forma de presentar el reporte puede quedar a discreción del
            #? programador, solo se pide como requisito que sea en un objeto que
            #? permita mostrar dicho reporte.
            

            for i, linea in enumerate(archivo, start = 1):
                reporte = [] #lista vacia 0,1,2,3,4,5,6
                for palabra in linea.split(): 
                    if palabra.isdigit():
                        reporte.append(int(palabra))
                for j , n1 in enumerate(reporte, start = 1):
                    if isinstance(n1, int):
                        binario = bin(n1)[2:]
                        print(f"linea {i}, numero {j}, binario {binario} ")
                    else:
                        print("No hay numeros en la linea")
                        break
        print("archivo creado")                




    except Exception as e:
        print("Error: ", e)



if __name__ == "__main__":
    main()