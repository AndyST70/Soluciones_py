#22. Realice un programa que manejando un archivo de texto (Entrada), muestre en pantalla la
#frecuencia de letras de dicho documento. El resultado de la frecuencia deberá mostrarlo además
#en un archivo de texto (salida).
#Requisitos:
#● La frecuencia debe mostrarla de la forma ordenada de “A” a “Z”.
#● Si la frecuencia de una letra es 0 no deberá mostrarla
#● La A, á, Á, a, debe contarla como una sola, al igual que las demás vocales (e, i, o, u).
#● La ñ y Ñ deberá contarla como una sola y mostrarla en el orden del alfabeto (después de la
#n).
#Ciclo 2024

import os
def contar_letras(texto):
    # Inicializar el diccionario para contar las letras
    frecuencia = {}

    # Convertir el texto a minúsculas para unificar las letras
    texto = texto.lower()

    # Definir las vocales a considerar como una sola
    vocales = ['a', 'e', 'i', 'o', 'u']

    # Contar la frecuencia de cada letra
    for letra in texto:
        if letra.isalpha():  # Verificar si es una letra
            if letra in vocales:  # Si es vocal, contarla como una sola
                letra = 'vocal'
            if letra == 'ñ':  # Contar la ñ como una sola
                letra = 'enye'
            frecuencia[letra] = frecuencia.get(letra, 0) + 1

    return frecuencia

def escribir_frecuencia(frecuencia, archivo_salida):
    # Ordenar las letras alfabéticamente
    letras_ordenadas = sorted(frecuencia.keys())

    # Escribir la frecuencia de cada letra en el archivo de salida
    with open(archivo_salida, 'w',encoding="utf-8") as archivo:
        for letra in letras_ordenadas:
            archivo.write(f"{letra}: {frecuencia[letra]}\n")

def main():
    archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    archivo_salida = input("Ingrese el nombre del archivo de salida: ")

    # Verificar si el archivo de entrada existe
    if not os.path.exists(archivo_entrada):
        print("El archivo de entrada no existe.")
        return

    # Leer el contenido del archivo de entrada
    with open(archivo_entrada, 'r', encoding="utf-8") as archivo:
        texto = archivo.read()

    # Contar la frecuencia de las letras en el texto
    frecuencia = contar_letras(texto)

    # Escribir la frecuencia en el archivo de salida
    escribir_frecuencia(frecuencia, archivo_salida)

    print("Frecuencia de letras guardada en el archivo de salida.")

    
if __name__ == "__main__":
    main()
