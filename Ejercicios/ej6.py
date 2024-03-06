#. Un alumno desea saber cuál será su calificación final en la materia de Computación. Dicha
# calificación se compone de los siguientes porcentajes:
# ● 55% del promedio de sus tres calificaciones parciales.
# ● 30% de la calificación del examen final.
# ● 15% de la calificación de un trabajo final.

#representar porcentajes
#? 0.55 = 55% EL PROMEDIO DE LAS 3 CALIFIACIONES
#? 0.3 = 30% EXAMEN FINAL
#? 0.15 = 15% TRABAJO FINAL
#! variables para nuetros programa
#* cal1, cal2, cal3, examen_final, trabajo_final
# todo Resolución de ejercicio 6
def main():
    print("Promedio de calificaciones")
    flag1 = True #booleano TRUE|FALSE
    while flag1:
        print("==================MENU======================")
        print("1. Ingresar calificaciones nuevo estudiante")
        print("2. Salir")
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            print("Ingresa califaciones")
            calculos()
        elif opc == 2:
            print("Saliendo del programa... ADIOS :D")
            flag1 = False

        else:
            print("Opcion no valida")
  

def calculos():
    cal1 = 0
    cal2 = 0
    cal3 = 0
    examen_final = 0
    trabajo_final = 0
    print("==========================")
    print("Ingrese sus calificaciones")
    cal1 = int(input("Calificacion 1: "))
    cal2 = int(input("Calificacion 2: "))
    cal3 = int(input("Calificacion 3: "))
    examen_final = int(input("Examen final: "))
    trabajo_final = int(input("Trabajo final: "))
    print("==========================")
    #? 0.55 = 55% EL PROMEDIO DE LAS 3 CALIFIACIONES
    #? 0.3 = 30% EXAMEN FINAL
    #? 0.15 = 15% TRABAJO FINAL
    #* calculo de porcentajes
    media = (cal1 + cal2 + cal3 )/ 3
    promedio = media * 0.55
    var_examen_final = examen_final * 0.3
    var_trabajo_Final = trabajo_final * 0.15
    suma_promedios = promedio + var_examen_final + var_trabajo_Final
    print("El promedio del estudiante ingresado es: ", suma_promedios)
if __name__ == "__main__":
    print("EJERCICIO 6")
    main()