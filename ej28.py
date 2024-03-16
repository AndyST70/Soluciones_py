#Desarrollar un programa que permita obtener los datos de empleados y los cálculos de
#prestaciones conforme a su salario mensual. Los campos para los registros son:
#Campos del registro Calcular Fórmulas para cálculos
#CODIGO DEL EMPLEADO
#NOMBRES COMPLETOS
#ÁREA O DEPARTAMENTO
#CARGO QUE OCUPA
#SUELDO BASE
#HORAS EXTRAS
#ANTICIPOS
#OTROS DESCUENTOS
#VALOR HORA EXTRA
#SUELDO EXTRA
#SUELDO BRUTO
#IGSS
##TOTAL DESCUENTOS
#SUELDO NETO
#BONIFICACIÓN
#SUELDO LÍQUIDO.
#Valor Hora Extra = (Sueldo Base/30/8)*1.5
#Sueldo Extra = Valor Hora Extra * Horas Extras
#Sueldo Bruto = Sueldo Base + Sueldo Extra
#IGSS = Sueldo Bruto * 4.83%
#Total Descuentos = IGSS + Anticipos + Otros
#Descuentos
#Sueldo Neto = Sueldo Bruto – Total Descuentos
#Bonificación = Sueldo Base * 10%
#Sueldo Líquido = Sueldo Neto + Bonificación
#● Grabar todos los datos ingresados y los calculados al archivo de tipo binario
#● Aplicar las 4 rutinas básicas (Ingreso, Consulta general, Consulta Individual)


def calcular_prestaciones(empleado):
    valor_hora_extra = (empleado[4] / 30 / 8) * 1.5
    sueldo_extra = valor_hora_extra * empleado[5]
    sueldo_bruto = empleado[4] + sueldo_extra
    igss = sueldo_bruto * 0.0483
    total_descuentos = igss + empleado[6] + empleado[7]
    sueldo_neto = sueldo_bruto - total_descuentos
    bonificacion = empleado[4] * 0.1
    sueldo_liquido = sueldo_neto + bonificacion
    
    return valor_hora_extra, sueldo_extra, sueldo_bruto, igss, total_descuentos, sueldo_neto, bonificacion, sueldo_liquido

def ingresar_empleado():
    codigo = input("Ingrese el código del empleado: ")
    nombres = input("Ingrese los nombres completos del empleado: ")
    area = input("Ingrese el área o departamento del empleado: ")
    cargo = input("Ingrese el cargo que ocupa el empleado: ")
    sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
    horas_extra = float(input("Ingrese las horas extra del empleado: "))
    anticipos = float(input("Ingrese los anticipos del empleado: "))
    otros_descuentos = float(input("Ingrese otros descuentos del empleado: "))
    
    return [codigo, nombres, area, cargo, sueldo_base, horas_extra, anticipos, otros_descuentos]

def guardar_empleados(empleados, archivo):
    with open(archivo, 'w') as f:
        for empleado in empleados:
            f.write(','.join(map(str, empleado)) + '\n')

def cargar_empleados(archivo):
    try:
        with open(archivo, 'r') as f:
            empleados = [line.strip().split(',') for line in f]
    except FileNotFoundError:
        empleados = []
    return empleados

def consulta_general(empleados):
    for empleado in empleados:
        print("Código:", empleado[0])
        print("Nombres completos:", empleado[1])
        print("Área o departamento:", empleado[2])
        print("Cargo que ocupa:", empleado[3])
        print("Sueldo base:", empleado[4])
        print("Horas extra:", empleado[5])
        print("Anticipos:", empleado[6])
        print("Otros descuentos:", empleado[7])
        print()

def consulta_individual(empleados, codigo):
    for empleado in empleados:
        if empleado[0] == codigo:
            print("Código:", empleado[0])
            print("Nombres completos:", empleado[1])
            print("Área o departamento:", empleado[2])
            print("Cargo que ocupa:", empleado[3])
            print("Sueldo base:", empleado[4])
            print("Horas extra:", empleado[5])
            print("Anticipos:", empleado[6])
            print("Otros descuentos:", empleado[7])
            print()
            return
    print("Empleado con código", codigo, "no encontrado.")

def main():
    empleados = cargar_empleados('empleados.txt')
    if not empleados:
        print("No se encontraron empleados en el archivo.")
        
    while True:
        print("1. Ingresar empleado")
        print("2. Consulta general")
        print("3. Consulta individual")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            empleado = ingresar_empleado()
            empleados.append(empleado)
            guardar_empleados(empleados, 'empleados.txt')
            print("Empleado ingresado exitosamente.")
        elif opcion == '2':
            consulta_general(empleados)
        elif opcion == '3':
            codigo = input("Ingrese el código del empleado: ")
            consulta_individual(empleados, codigo)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()




