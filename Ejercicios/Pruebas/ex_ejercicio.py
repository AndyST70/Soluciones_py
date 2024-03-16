import random
import tkinter as tk
from tkinter import messagebox

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
    if 0 <= posicion < len(vector):
        vector[posicion] = nuevo_numero
    else:
        messagebox.showerror("Error", "La posición especificada está fuera de rango.")


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

# Función principal
def main():
    # Función para manejar el evento del botón "Aceptar" en la ventana principal
    def aceptar_click():
        largo = int(entrada_largo.get())
        vector1, vector2 = crear_vectores(largo)
        etiqueta_vector1.config(text="Vector 1: " + str(vector1))
        etiqueta_vector2.config(text="Vector 2: " + str(vector2))
        
        objetivo1 = int(entrada_objetivo1.get())
        objetivo2 = int(entrada_objetivo2.get())
        resultado_busqueda1 = busqueda_binaria(vector1, objetivo1)
        resultado_busqueda2 = busqueda_binaria(vector2, objetivo2)
        if resultado_busqueda1 != -1:
            messagebox.showinfo("Resultado", f"El número {objetivo1} se encuentra en la posición {resultado_busqueda1} del primer vector.")
        else:
            messagebox.showinfo("Resultado", f"El número {objetivo1} no se encuentra en el primer vector.")
        if resultado_busqueda2 != -1:
            messagebox.showinfo("Resultado", f"El número {objetivo2} se encuentra en la posición {resultado_busqueda2} del segundo vector.")
        else:
            messagebox.showinfo("Resultado", f"El número {objetivo2} no se encuentra en el segundo vector.")
        
        posicion1 = int(entrada_posicion1.get())
        nuevo_numero1 = int(entrada_nuevo_numero1.get())
        posicion2 = int(entrada_posicion2.get())
        nuevo_numero2 = int(entrada_nuevo_numero2.get())
        reemplazar_numero(vector1, posicion1, nuevo_numero1)
        reemplazar_numero(vector2, posicion2, nuevo_numero2)
        etiqueta_vector1_actualizado.config(text="Primer vector actualizado: " + str(vector1))
        etiqueta_vector2_actualizado.config(text="Segundo vector actualizado: " + str(vector2))
        
        suma = sumar_vectores(vector1, vector2)
        etiqueta_suma.config(text="Suma de vectores: " + str(suma))
        
        resta = restar_vectores(vector1, vector2)
        etiqueta_resta.config(text="Resta de vectores: " + str(resta))
        
        suma_base16 = a_base16(suma)
        etiqueta_suma_base16.config(text="Suma de vectores en base 16: " + str(suma_base16))
        
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Programa con Tkinter")
    
    # Crear etiquetas y entradas para los parámetros
    etiqueta_largo = tk.Label(ventana, text="Largo de los vectores:")
    etiqueta_largo.grid(row=0, column=0)
    entrada_largo = tk.Entry(ventana)
    entrada_largo.grid(row=0, column=1)
    
    etiqueta_objetivo1 = tk.Label(ventana, text="Objetivo para el primer vector:")
    etiqueta_objetivo1.grid(row=1, column=0)
    entrada_objetivo1 = tk.Entry(ventana)
    entrada_objetivo1.grid(row=1, column=1)
    
    etiqueta_objetivo2 = tk.Label(ventana, text="Objetivo para el segundo vector:")
    etiqueta_objetivo2.grid(row=2, column=0)
    entrada_objetivo2 = tk.Entry(ventana)
    entrada_objetivo2.grid(row=2, column=1)
    
    etiqueta_posicion1 = tk.Label(ventana, text="Posición para reemplazar en el primer vector:")
    etiqueta_posicion1.grid(row=3, column=0)
    entrada_posicion1 = tk.Entry(ventana)
    entrada_posicion1.grid(row=3, column=1)
    
    etiqueta_nuevo_numero1 = tk.Label(ventana, text="Nuevo número para el primer vector:")
    etiqueta_nuevo_numero1.grid(row=4, column=0)
    entrada_nuevo_numero1 = tk.Entry(ventana)
    entrada_nuevo_numero1.grid(row=4, column=1)
    
    etiqueta_posicion2 = tk.Label(ventana, text="Posición para reemplazar en el segundo vector:")
    etiqueta_posicion2.grid(row=5, column=0)
    entrada_posicion2 = tk.Entry(ventana)
    entrada_posicion2.grid(row=5, column=1)
    
    etiqueta_nuevo_numero2 = tk.Label(ventana, text="Nuevo número para el segundo vector:")
    etiqueta_nuevo_numero2.grid(row=6, column=0)
    entrada_nuevo_numero2 = tk.Entry(ventana)
    entrada_nuevo_numero2.grid(row=6, column=1)
    
    # Botón para ejecutar el programa
    boton_aceptar = tk.Button(ventana, text="Aceptar", command=aceptar_click)
    boton_aceptar.grid(row=7, columnspan=2)
    
    # Etiquetas para mostrar los resultados
    etiqueta_vector1 = tk.Label(ventana, text="")
    etiqueta_vector1.grid(row=8, columnspan=2)
    
    etiqueta_vector2 = tk.Label(ventana, text="")
    etiqueta_vector2.grid(row=9, columnspan=2)
    
    etiqueta_vector1_actualizado = tk.Label(ventana, text="")
    etiqueta_vector1_actualizado.grid(row=10, columnspan=2)
    
    etiqueta_vector2_actualizado = tk.Label(ventana, text="")
    etiqueta_vector2_actualizado.grid(row=11, columnspan=2)
    
    etiqueta_suma = tk.Label(ventana, text="")
    etiqueta_suma.grid(row=12, columnspan=2)
    
    etiqueta_resta = tk.Label(ventana, text="")
    etiqueta_resta.grid(row=13, columnspan=2)
    
    etiqueta_suma_base16 = tk.Label(ventana, text="")
    etiqueta_suma_base16.grid(row=14, columnspan=2)
    
    ventana.mainloop()

if __name__ == "__main__":
    main()
