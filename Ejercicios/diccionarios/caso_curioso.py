#El método keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']


#El método values() devuelve una lista con todos los values o valores del diccionario.
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

#El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Daría un error si se intenta eliminar una key que no existe.
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}

#elimina aleatoriamente un tiem
d = {'a': 1, 'b': 2}
d.popitem()
print(d)
#{'a': 1}



#actuailiza y si no existe la crea
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1)
#{'a': 0, 'b': 2, 'd': 400}