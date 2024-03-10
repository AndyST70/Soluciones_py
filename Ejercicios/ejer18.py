#18. Escriba un programa que pida el ingreso de un número entre 1 y 99,999 y muestre en español la
#cantidad equivalente. Observe que los números tienden a repetirse y recuerde que novecientos,
#setecientos son casos especiales


def numero_a_palabras(numero):
    unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    especiales = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']

    if 0 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return especiales[numero - 10]
    elif 20 <= numero <= 99:
        decena = decenas[(numero // 10) - 2]
        unidad = unidades[numero % 10]
        if numero % 10 == 0:
            return decena
        else:
            return decena + ' y ' + unidad
    elif 100 <= numero <= 99999:
        pass  
    else:
        return "Número fuera de rango"

def main():
    numero = int(input("Ingrese un número entre 1 y 99,999: "))

    if 1 <= numero <= 99999:
        resultado = numero_a_palabras(numero)
        print(f"El número {numero} en español es: {resultado}")
    else:
        print("Número fuera de rango")

if __name__ == "__main__":
    main()
