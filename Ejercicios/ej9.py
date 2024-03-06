
#9. Realizar un programa que calcule la edad de una persona de acuerdo a la fecha de nacimiento.

import datetime

def main():
    print("CALCULO DE EDAD :D")
    print("Ingrese su fecha de nacimiento")
    print("Dia: ")
    dia = int(input("-> "))
    print("Mes: ")
    mes = int(input("-> "))
    print("Año: ")
    año = int(input("-> "))

    if mes >= 12 or mes <= 1:
        print("Mes invalido")
        return
    if dia > 31 or dia < 1:
        print("Dia invalido")
        return
    if año > datetime.datetime.now().year:
        print("Año invalido")
        return

    fecha_nacimiento = datetime.datetime(año, mes, dia)
    fecha_actual = datetime.datetime.now() #obtenenido la fecha actual
    edad = fecha_actual.year - fecha_nacimiento.year

    # Verificar si ya pasó el cumpleaños este año
    if (fecha_nacimiento.month, fecha_nacimiento.day) > (fecha_actual.month, fecha_actual.day):
        edad -= 1

    print("Su edad es: ", edad)
    return

if __name__ == "__main__":
    print("Ejercicio 9")
    main()