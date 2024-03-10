lista = [1, 8,5, 9,0, 6, 4]

def separacion(lista):
    if len(lista)<1:
        return []
    izquierda = []
    derecha = []
    pivote = lista[0]

    for i in range (1, len(lista)):
        if lista[i]<pivote:
            izquierda.append(lista[i])
            print(lista)
        else:
            derecha.append(lista[i])
            print(lista)
    return izquierda, pivote, derecha


def quicksort(lista):
    if len(lista)<2:
        return lista
    
    izquierda, pivote, derecha = separacion(lista)
    return quicksort(izquierda)+[pivote]+quicksort (derecha)
print(quicksort(lista))