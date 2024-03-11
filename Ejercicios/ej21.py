#21. Escriba un programa que vaya leyendo las frases que el usuario escribe y que las guarde
#conforme se escribe en un archivo de texto llamado frases.txt, el programa deja de grabar
#cuando se ingrese la palabra
#“Fin”. (Esa palabra no se guarda en el archivo)

def main():
    archivo = open("frases.txt", "w", encoding="utf-8")
    #ingrese una palabra
    #ingrese otra palbra
    #ingresera una tercera frase

    while True:
        frase = input("Ingrese una frase: ")
        if frase == "Fin":
            break
        archivo.write(frase + "\n")
    archivo.close()
    print("Archivo creado con exito")

if __name__ == "__main__":
    main()