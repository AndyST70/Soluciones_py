"""Instrucciones para Convertir de Decimal a Base 16 (hex):
1. Divide el número decimal entre 16.
2. Guarda el residuo.
3. Divide el cociente obtenido en el paso anterior entre 16.
4. Guarda el nuevo residuo.
5. Repite los pasos 3 y 4 hasta que el cociente sea 0.
6. Lee los residuos en orden inverso para obtener el número en base 16.
7. Si un residuo es mayor o igual a 10, reemplázalo con la letra correspondiente en
base 16 (A=10, B=11, ..., F=15)."""

#se importan las librerias necesarias
from tkinter import*
import tkinter as tk
import random
from tkinter import messagebox

def generarvector():
    global v1, v2
    largo = int(entrylargo.get())  # Obtener el largo desde la entrada de texto
    v1 = []
    v2 = []
    for _ in range(largo):
        v1.append(random.randint(1, 100))
        v2.append(random.randint(1, 100))

    messagebox.showinfo("vectores generados", f"\nvector #1: {v1} \n vector #2: {v2}")
    
def mostrarvectores(largo):
    return[random.randint(1, 100) for _ in range(largo)]

def sumavectores(v1, v2):
    return[x + y for x, y in zip(v1, v2)]

def base16(vector):
    hex= ""
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexa = str(residuo) + hex
        else: 
            hex = chr(ord("a")+residuo - 10) + hex
        numero //= 16
    return hex if hex else 0 

def mostrarvectores():
    messagebox.showinfo("vectores generados", "\nvector #1: {v1} \n vector #2: {v2}")
    
def operaryconvertir():
    resultado = sumavectores(v1, v2)
    resultadohexa = base16(sum(resultado))
    messagebox.showinfo("el resultado es:", "/n suma: {resultado} /n base 16: {resultadohexa}")

v = tk.Tk()
v.title("operaciones de vectores")

lbllargo=tk.Label(v, text="largo de los vectores: ")
lbllargo.pack()

entrylargo = tk.Entry(v)
entrylargo.pack()

btngenerar = tk.Button(v, text="generar vectores", command=generarvector)
btngenerar.pack()

btnmostrar = tk.Button(v, text="mostrar vectores", command=mostrarvectores)
btnmostrar.pack()

btnoperar = tk.Button(v, text="sumar y convertir a base 16")
btnoperar.pack()

v1 = []
v2 = []

v.mainloop()