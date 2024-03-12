#24. Escriba un programa que permita escribir un párrafo en un archivo de texto, luego en un vector
#ingresar 5 palabras a buscar.
#Las palabras deben localizarse en el archivo de texto, si la palabra existe en el archivo colocarla
#en un nuevo vector y luego mostrar el número de veces que esta palabra se encontró dentro del
#archivo de texto.

#archivo tipo vector 5 palabras
#archivo tipo vector 5 palabras encontradas

def main():

    print("ESCRIBE UN PARRAFO COMPLETO POR FAVOR")
    parrafo = input()
    try:
        with open("create_Archivo.txt", "w", encoding="utf-8") as file:
            file.write(parrafo)
        print("Archivo creado con exito")
    except Exception as e:
        print("Error: ", e)
    buscar_palabras()

def buscar_palabras():
    palabras = []
    palabras_encontradas = []
    for i in range(5):
        palabras.append(input("Ingrese una palabra: "))
    
    try:
        with open("create_Archivo.txt", "r", encoding="utf-8") as archivo:
            texto = archivo.read() #leer el archivo
            for palabra in palabras: #recorrer el vector de palabras
                if palabra in texto: #si existe la palabra en el texto
                    palabras_encontradas.append(palabra) #agregar la palabra al vector de palabras encontradas
            
                    print("La palabra ", palabra, " fue encontrada ", texto.count(palabra), " veces")
            
    except Exception as e:
        print("Error: ", e)

 

if __name__ == "__main__":
    main()