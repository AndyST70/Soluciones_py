import time
import datetime
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Reloj con Python y Tkinter")

etiqueta_hora = tk.Label(ventana, font=("Arial", 24), bg="white")
etiqueta_hora.pack(pady=50)

def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")
    etiqueta_hora.config(text=hora_actual)
    ventana.after(1000, actualizar_hora)

actualizar_hora()
ventana.mainloop()