import tkinter as tk
from tkinter import filedialog

def main():
    try:
        root = tk.Tk()
        root.withdraw()  

        filepath = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[("Archivos de texto", ".txt"), ("Todos los archivos", ".*")]
        )

        if not filepath: 
            print("No se seleccionó ningún archivo.")
            return

        with open(filepath, "r", encoding="utf-8") as archivo:
            for i, linea in enumerate(archivo, start=1):
                reporte = []
                for palabra in linea.split():
                    if palabra.isdigit():
                        reporte.append(int(palabra))
                for j, num in enumerate(reporte, start=1):
                    binario = bin(num)[2:]  
                    print(f"linea {i}, numero {j}, binario {binario}")

        print("archivo procesado")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()