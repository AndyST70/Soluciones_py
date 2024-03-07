#13. Una universidad estableció un programa para estimular a los estudiantes con buen rendimiento
#académico y que consiste en lo siguiente:
#Si el promedio es de 8.5 o más, entonces se le hará un 30% de descuento en la matrícula.
#Si el promedio es mayor o igual a 7 pero menor que 8.5 entonces se le hará un 10% de
#descuento.
#Si el promedio es mayor que 5.5 y menor que 7, no tendrá ningún descuento.
#Obtener el total que tendrá que pagar un estudiante de acuerdo a su matrícula y promedio
#actual.


def main():
    print("Descuento por estudiante y buenas calificaciones")
    flag1 = True
    while flag1:
        print("==================MENU======================")
        print("1. Ingresar estudiante")
        print("2. Salir")
        opc = int(input("Ingrese una opción: "))
        if opc == 1:
            print("Ingresa calificaciones")
            nombre = input("Ingrese el nombre del estudiante: ")
            matricula = float(input("Ingrese el monto de la matrícula: "))
            promedio = float(input("Ingrese el promedio del estudiante: "))
            calculos(nombre, matricula, promedio)
        elif opc == 2:
            print("Saliendo del programa... ADIOS :D")
            flag1 = False
        else:
            print("Opción no válida")

def calculos(nombre, matricula, promedio):
    descuento = 0
    total_pagar = 0
    
    if promedio >= 8.5:
        descuento = 0.30 * matricula
    elif promedio >= 7 and promedio < 8.5:
        descuento = 0.10 * matricula
    
    total_pagar = matricula - descuento
    
    print(f"Estudiante: {nombre}")
    print(f"Descuento: Q{descuento:.2f}")
    print(f"Total a pagar: Q{total_pagar:.2f}")

if __name__ == '__main__':
    print("Ejercicio 13: Descuento por estudiante")
    main()
