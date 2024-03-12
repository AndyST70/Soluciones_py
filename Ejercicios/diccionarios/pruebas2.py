

#DICCIONARIOS en python

#Se caracterizan por tener una llave y un valor respectivo

diccionario1 = {
    "nombre": "name1",
    "edad": 50
}

print(diccionario1)

#Tambien está la funcion dict() que crea un diccionario con elementos
lista = [('Nombre', 'usr1'),('Edad', 50),('Pais', "Guatemala")]
diccionario = dict(lista)

print(diccionario)

#Obtener por llave/atributo

print(diccionario["Nombre"]) #Muestra el valor, en este caso usr1

#Ventaja de ser flexible, se puede agregar un valor no incluido
diccionario["Estatura"] = "125"
print(diccionario)


#Recorrer con for
for valor in diccionario: #Esto imprime las llaves
    print(valor)

for valor in diccionario: #Esto imprime los valores
    print(diccionario[valor])    

for x, y in diccionario.items(): #Imprime ambos
    print(x, y)

    