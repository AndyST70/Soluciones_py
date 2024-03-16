def unir_archivos(archivo1, archivo2, archivo3):
    try:
        with open(archivo1, 'r', encoding='utf-8') as file1, \
             open(archivo2, 'r', encoding='utf-8') as file2, \
             open(archivo3, 'w', encoding='utf-8') as file3:
            
            for linea1, linea2 in zip(file1, file2):
                linea_combinada = linea1.strip() + " " + linea2.strip() + "\n"
                file3.write(linea_combinada)
            
            print("Archivos combinados exitosamente.")
    except FileNotFoundError:
        print("Error: No se pudo encontrar uno o ambos archivos.")


def main():
    archivo1 = "archivo1.txt"
    archivo2 = "archivo2.txt"
    archivo3 = "archivo3.txt"

    unir_archivos(archivo1, archivo2, archivo3)


if __name__ == "__main__":
    main()