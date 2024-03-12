#27. Desarrollar un programa que permita llevar el control de una agenda para N contactos. Los
#campos para el almacenamiento de datos son:
#● Número de contacto
#● Nombre completo
#● Dirección
#● Teléfono móvil
#● Teléfono de casa
#● Correo electrónico
#El programa debe ser capaz de almacenar los datos en una estructura y luego grabarla a un
#archivo binario para darle acceso directo a los diferentes registros.
#El número de contacto equivale al número de registro en el que se almacenan los datos.
#● Validar s


import pickle
import os

def crear_agenda():
    agenda = {}
    return agenda

def agregar_contacto(agenda, numero, nombre, direccion, telefono_movil, telefono_casa, correo):
    agenda[numero] = {
        'Nombre': nombre,
        'Dirección': direccion,
        'Teléfono móvil': telefono_movil,
        'Teléfono de casa': telefono_casa,
        'Correo electrónico': correo
    }

def mostrar_contactos(agenda):
    for numero, contacto in agenda.items():
        print(f"Número de contacto: {numero}")
        for campo, valor in contacto.items():
            print(f"{campo}: {valor}")
        

def guardar_agenda(agenda, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(agenda, archivo)

def cargar_agenda(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'rb') as archivo:
            return pickle.load(archivo)
    else:
        print("El archivo no existe.")
        return None

def main():
    nombre_archivo = "agenda.dat"

    if os.path.exists(nombre_archivo):
        respuesta = input("El archivo de agenda ya existe. ¿Desea sobreescribirlo? (S/N): ")
        if respuesta.lower() != 's':
            return

    agenda = crear_agenda()

    while True:
        print("\nMenú:")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Guardar agenda en archivo binario")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            numero = input("Número de contacto: ")
            nombre = input("Nombre completo: ")
            direccion = input("Dirección: ")
            telefono_movil = input("Teléfono móvil: ")
            telefono_casa = input("Teléfono de casa: ")
            correo = input("Correo electrónico: ")
            agregar_contacto(agenda, numero, nombre, direccion, telefono_movil, telefono_casa, correo)
        elif opcion == '2':
            mostrar_contactos(agenda)
        elif opcion == '3':
            guardar_agenda(agenda, nombre_archivo)
            print("Agenda guardada correctamente en el archivo binario.")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
