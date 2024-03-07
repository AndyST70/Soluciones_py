
#Vectores
# Se puede almacenar datos en ellos, 
# conforme se va almacenando la información se va reservando memoria para 
# la cantidad de datos guardados.


a = [] #en python se pueden almacenar valores de diferente tipo

b = [5,"Hola",3.2,True]
print(b)
print(b[3])

#Se puede reasignar la informacion accediendo a una posicion especifica
# tomando de referencia b, 
# b tiene 4 elementos, su tamaño será 4 pero siempre se inicia a contar
# desde 0. 

#Para acceder a un elemento especifico se usa el índice, este puede ser
#un numero entero explicito o bien, una variable entera, útil en muchos casos
#donde no se tiene el valor exacto o es cambiante dentro del flujo del programa.
# 0, 1 , 2 , 3
print(b[0])

for i in range(0,len(b)): #En python len() devuelve el tamaño de un vector o string, este será de 4 pero 
    print(b[i])           #el índice siempre irá de 0 a 4 en este ejemplo.  

#[5,"Hola",3.2,True]
#Se puede reasignar un valor especifico
print(b) #original
b[2] = "NUEVO"
print(b) #modificado

#Funciones nativas de python más comunes, existen otras

b.append(100)  #Append agrega nuevo valor al final
b.clear() #Clear vacía la informacion 
b.pop() #Extrae el ultimo valor del vector, útil para trabajar con pilas






