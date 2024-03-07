#12. Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
#● Si trabaja 40 horas o menos se le paga Q20 por hora
#● Si trabaja más de 40 horas se le paga Q20 por cada una de las primeras 40 horas y Q25
#por cada hora extra.


#* variables : obrero, salario_semanal, horas_Trabajadas, horas_Extras
#? 1. 40 horas o menos se le paga Q20 por hora
#? 2. Si trabaja más de 40 horas se le paga Q20 por cada una de las primeras 40 horas y Q25 por cada hora extra.
def main():
    print("Salario semanal")
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    salario_total = calculos(horas_trabajadas)
    print("Salario total: Q", salario_total)

def calculos(hor_trabajadas):
    total = 0
    salario = 20
    extra_salario = 25
    horas_Extras = 0
    horas_noramles = 0
    
    if hor_trabajadas <= 40:
        total = hor_trabajadas * salario
    else: 
        horas_Extras = hor_trabajadas - 40
        horas_noramles = 40  
        total = (horas_noramles * salario) + (horas_Extras * extra_salario)
        print("Horas normales:", horas_noramles)
    
    return total  # Devolver el salario total

if __name__ == '__main__':
    print("Ejercicio 12: Salario semanal")
    main()