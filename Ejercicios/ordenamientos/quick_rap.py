def quicksort(lista):
    if len(lista) < 2:
        return lista

    pivote = lista[0]
    izquierda = []
    derecha = []

    for i in lista[1:]:
        if i < pivote:
            izquierda.append(i)
        else:
            derecha.append(i)

    return quicksort(izquierda) + [pivote] + quicksort(derecha)

# Ejemplo de uso
lista = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(lista))