import random
# Función para crear vectores aleatorios
def crear_vectores(largo):
    vector1 = []
    vector2 = []
    for _ in range(largo):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        vector1.append(num1)
        vector2.append(num2)
    return vector1, vector2 

# Función para buscar un número en un vector utilizando búsqueda binaria
def busqueda_binaria(vector, objetivo):
    izquierda, derecha = 0, len(vector) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if vector[medio] == objetivo:
            return medio
        elif vector[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Función para reemplazar un número en un vector
def reemplazar_numero(vector, posicion, nuevo_numero):
    vector[posicion] = nuevo_numero

# Función para realizar la suma de dos vectores
def sumar_vectores(vector1, vector2):
    resultado = []
    for i in range(len(vector1)):
        resultado.append(vector1[i] + vector2[i])
    return resultado

# Función para realizar la resta de dos vectores
def restar_vectores(vector1, vector2):
    resultado = []
    for i in range(len(vector1)):
        resultado.append(vector1[i] - vector2[i])
    return resultado

# Función para convertir un vector a base 16
def a_base16(vector):
    resultado = []
    for num in vector:
        residuos = []
        while num > 0:
            residuo = num % 16
            if residuo >= 10:
                residuo = chr(ord('A') + residuo - 10)  # Convertir a letra si es mayor o igual a 10
            residuos.append(str(residuo))
            num //= 16
        resultado.append("0x" + "".join(residuos[::-1]))  # Concatenar residuos en orden inverso
    return resultado

def main():
    # Pedir al usuario el largo de los vectores
    largo = int(input("Ingrese el largo de los vectores: "))
    
    # Crear los vectores aleatorios
    vector1, vector2 = crear_vectores(largo)
    
    # Mostrar los vectores
    print("Vector 1:", vector1)
    print("Vector 2:", vector2)

    
    # Pedir al usuario el número a buscar en cada vector
    objetivo1 = int(input("Ingrese un número para buscar en el primer vector: "))
    objetivo2 = int(input("Ingrese un número para buscar en el segundo vector: "))
    
    # Realizar la búsqueda binaria en cada vector
    resultado_busqueda1 = busqueda_binaria(vector1, objetivo1)
    resultado_busqueda2 = busqueda_binaria(vector2, objetivo2)
    
    # Mostrar resultados de búsqueda
    if resultado_busqueda1 != -1:
        print(f"El número {objetivo1} se encuentra en la posición {resultado_busqueda1} del primer vector.")
    else:
        print(f"El número {objetivo1} no se encuentra en el primer vector.")
    
    if resultado_busqueda2 != -1:
        print(f"El número {objetivo2} se encuentra en la posición {resultado_busqueda2} del segundo vector.")
    else:
        print(f"El número {objetivo2} no se encuentra en el segundo vector.")
    
    # Pedir al usuario el número a reemplazar en cada vector
    posicion1 = int(input("Ingrese la posición en el primer vector para reemplazar: "))
    nuevo_numero1 = int(input("Ingrese el nuevo número para colocar en el primer vector: "))
    posicion2 = int(input("Ingrese la posición en el segundo vector para reemplazar: "))
    nuevo_numero2 = int(input("Ingrese el nuevo número para colocar en el segundo vector: "))
    
    # Reemplazar números en cada vector
    reemplazar_numero(vector1, posicion1, nuevo_numero1)
    reemplazar_numero(vector2, posicion2, nuevo_numero2)
    
    # Mostrar vectores actualizados
    print("Primer vector actualizado:", vector1)
    print("Segundo vector actualizado:", vector2)
    
    # Realizar suma de vectores
    suma = sumar_vectores(vector1, vector2)
    print("Suma de vectores:", suma)
    
    # Realizar resta de vectores
    resta = restar_vectores(vector1, vector2)
    print("Resta de vectores:", resta)
    
    # Convertir la suma a base 16
    suma_base16 = a_base16(suma)
    print("Suma de vectores en base 16:", suma_base16)

if __name__ == "__main__":
    main()

