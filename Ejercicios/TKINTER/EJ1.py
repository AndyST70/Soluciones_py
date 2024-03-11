import tkinter as tk

root = tk.Tk()

# Creamos un cuadro de texto
entry = tk.Entry(root)

# Creamos un botón
button = tk.Button(root, text="Enviar")

# Posicionamos los elementos en la ventana
entry.pack()
button.pack()

# Mostramos la ventana
root.mainloop()