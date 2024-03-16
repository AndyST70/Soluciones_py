import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def abrir_archivo(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            numeros = []
            for linea in file:
                elementos = linea.split('-')
                linea_numeros = []
                for num in elementos[1:]:
                    num_limpio = num.strip()
                    if num_limpio:
                        try:
                            numero_flotante = float(num_limpio)
                            linea_numeros.append(numero_flotante)
                        except ValueError:
                            pass
                numeros.append(linea_numeros)
            return numeros
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo.")
    except Exception as e:
        print(f"Error: {e}")

def calcular_sumatorias(numeros):
    sumatorias_horizontales = []
    for fila in numeros:
        suma_fila = sum(fila)
        sumatorias_horizontales.append(suma_fila)

    sumatorias_verticales = []
    for i in range(len(numeros[0])):
        suma_vertical = sum(fila[i] for fila in numeros)
        sumatorias_verticales.append(suma_vertical)

    return sumatorias_horizontales, sumatorias_verticales


def mostrar_resultado(numeros, sumatorias_horizontales, sumatorias_verticales):
    root = tk.Tk()
    root.title("Reporte de sumatorias")

    tree = ttk.Treeview(root)
    tree["columns"] = ("1", "2", "3", "4", "5", "Totales")

    tree.heading("#0", text=" ")
    tree.heading("1", text="1")
    tree.heading("2", text="2")
    tree.heading("3", text="3")
    tree.heading("4", text="4")
    tree.heading("5", text="5")
    tree.heading("Totales", text="Totales")

    # Mostrar números y sumatorias horizontales
    for i, (fila, suma_horizontal) in enumerate(zip(numeros, sumatorias_horizontales), start=1):
        fila_tree = [f"{num:.2f}" for num in fila] + [f"{suma_horizontal:.2f}"]
        tree.insert("", tk.END, text=str(i), values=fila_tree)

    # Mostrar sumatorias verticales y total horizontal
    total_horizontal = sum(sumatorias_horizontales)
    suma_vertical_text = [f"{suma_vertical:.2f}" for suma_vertical in sumatorias_verticales]
    total_horizontal_text = [f"{total_horizontal:.2f}"]
    tree.insert("", tk.END, text="Totales", values=suma_vertical_text + total_horizontal_text)

    tree.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

def main():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        numeros = abrir_archivo(archivo)
        if numeros:
            sumatorias_horizontales, sumatorias_verticales = calcular_sumatorias(numeros)
            mostrar_resultado(numeros, sumatorias_horizontales, sumatorias_verticales)

if __name__ == "__main__":
    main()
