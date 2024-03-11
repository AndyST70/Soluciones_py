#20. Elaborar un programa que muestre un número decimal menor a 4000 en su correspondiente
#número romano. Para interpretar los números romanos hay que tener en cuenta una serie de
#reglas que os detallamos a continuación:
#● Los símbolos se escriben y se leen de izquierda a derecha, poniendo primero los de mayor
#valor.
#● El valor del número romano se obtiene sumando los valores de los símbolos, sin embargo,
#existe una excepción en la que, si un símbolo está a la izquierda de uno más grande,
#entonces restamos el valor del número más pequeño al número más grande (ejemplo: IV = 5
#-1 = 4).
#● El símbolo para el número 5 (V) siempre suman y no se pueden colocar a la izquierda de uno
#más grande. Además, no se puede colocar de forma consecutiva dos veces ya que para eso
#existe el número 10 en romano (X)
#● El símbolo del 1 (I) sólo se puede repetir como máximo tres veces de forma consecutiva en
#un mismo número romano.
#● En las restas hay que tener en cuenta que:
#o El 1 (I) sólo puede restar a los símbolos V y X
#o El 10 (X) sólo puede restar a L y C
#o El 100 (C) sólo puede restar a D y M
#● Además, se permite que dos símbolos diferentes aparezcan restando si no son adyacentes.
#● Ejemplos:
#o 2015 en números romanos: MMXV
#o 99 en números romanos: XCIX
#o 49 en números romanos: XLIX
#o 500 en números romanos: D
#o 19 en números romanos: XIX

def main():
    print("Ejercicio 20")
    numero = int(input("Ingrese un número decimal menor a 4000: "))
    var_number = numero_a_romanos(numero)
    if numero < 1 or numero >= 4000:
        print("El número ingresado no es válido")
        return
    else:
        print(f"El número romano es: {var_number}")
    

def numero_a_romanos(numero):
    valores = [(1000, "M"), (900, "CM"), 
               (500, "D"), (400, "CD"), 
               (100, "C"), (90, "XC"), 
               (50, "L"), (40, "XL"), 
               (10, "X"), (9, "IX"), 
               (5, "V"), (4, "IV"), 
               (1, "I")]
    romanos = ""

    for val, i in valores:
        while numero >= val:
            numero -= val
            romanos += i
    return romanos
    #I II III IV V

if __name__ == "__main__":
    main()