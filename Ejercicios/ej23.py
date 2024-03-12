#23. Escriba un programa que permita al usuario guardar un bloque de texto en un archivo, luego
#permita abrirlo nuevamente y mediante un botón llamado “Revisión” muestre en pantalla la
#cantidad de letras, palabras y líneas que contiene el archivo creado.

#? escribir nuestro archivo de texto (w)
#? leer nuestro archivo de texto    (r)
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ejercjcio 23")

entrada_text = tk.Text(ventana, height=10, width=50)
entrada_text.pack()

guardar_boton = tk.Button(ventana, text="Guardar", command=lambda: guardar())
guardar_boton.pack(pady=2)


boton_revision = tk.Button(ventana, text="Revisión", command=lambda: revision())
boton_revision.pack(pady=2)


#? escribir nuestro archivo de texto (w)
#? leer nuestro archivo de texto    (r)
def guardar():
    print("Guardando...")
    texto = entrada_text.get("1.0", tk.END)
    try:
        with open("text_guardado.txt", "w", encoding="utf-8") as archivo:
            archivo.write(texto)
        messagebox.showinfo("Guardado", "El archivo se guardo correctamente")    
    except Exception as e:
        messagebox.showerror("Error", "No se pudo guardar el archivo")


#todo cantidad de letras, palabras lineas
def revision():
    print("Revisando...")
    try:
        with open("text_guardado.txt", "r", encoding="utf-8") as archivo:
            texto = archivo.read()
            letras = len(texto) #string, y lo que ara es que obtendra el tamaño del string
            palabras = len(texto.split()) #split() separa las palabras por espacio, ";", ",", "_" etc
            lineas = texto.count("\n") + 1 #cuenta los saltos de linea
            messagebox.showinfo("Revisión", f"El archivo contiene:\n{letras} letras\n{palabras} palabras\n{lineas} lineas")
    except Exception as e:
        messagebox.showerror("Error", "No se pudo abrir el archivo")

ventana.mainloop()