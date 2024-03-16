#Ejercicio 2:
#Desarrolla un programa que permita al usuario ingresar una lista de nombres de personas
# y sus edades separados por comas. Guarda esta información en un archivo de texto llamado 
#"personas.txt". Luego, lee el archivo y muestra en pantalla el nombre de la persona con 
#la edad más alta.

def main():
    escribir()

def escribir():
    personas = input("Ingresa los nombres de personas y edades separadas por coma: ")
    with open("personas.txt", "w", encoding="utf-8") as archivo:
        archivo.write(personas)
    leer()
def leer():
    try:
        with open("personas.txt", "r", encoding="utf-8") as archivo:
            lista = archivo.read().split(",")
            diccionario_personas = {}
            for i in lista:
                name, age= i.strip().split() # lisat : ["nombre", "edad], i ["nombre"] , ["edad"]
                #age = int(lista[i+1].strip())
                diccionario_personas[name] = age
            edad_mayor = max(diccionario_personas, key=diccionario_personas.get)
            print("la persona mas grande es :", edad_mayor)
    except FileNotFoundError:
        print("No se encontro el archivo")
if __name__ == "__main__":
    main()