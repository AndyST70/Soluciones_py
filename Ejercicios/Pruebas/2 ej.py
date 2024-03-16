#Desarrolle un programa que permita abrir los dos archivos de acceso secuencial 
#observe el ejemplo:

#abrir archivos
def main():
    print("Abriendo archivo 1")
    archivo1 = "archivo1.txt"
    archivo2 = "archivo2.txt"
    unir_archivos(archivo1, archivo2)


def unir_archivos(arc_1, arc_2):
    try :
        with open(arc_1, "r", encoding="utf-8") as archivo1, \
             open(arc_2, "r", encoding="utf-8") as archivo2, \
             open("archivo3.txt", "w", encoding="utf-8") as archivo3:
                for linea1, linea2 in zip(archivo1, archivo2):
                    linea_combinada = linea1.strip() + " " +linea2.strip() + "\n"
                    archivo3.write(linea_combinada)
        print("Archivos unidos")

    except FileNotFoundError:
        print("No se encontro el archivo")

if __name__ == "__main__":
    main()

#COMPU -> ESTO VA VENIREN EL EXAMEN
#generar 2 vectores con random, ordenarlos con sort de conteo y sort de insercion
#unir el vector 1 y vector 2 y los sumados elevarlo a base 16
#necesita pseudocodigo pero solo los sorts
    
#un analisis del programa
#entrada salida y proceso
