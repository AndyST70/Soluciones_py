#FORMATEO E HORAS COMO CADENAS DE TEXTO
import datetime

fecha = datetime.datetime(2022, 12, 25)
fecha_formateada = fecha.strftime("%d/%m/%Y")
print("Fecha formateada:", fecha_formateada)
