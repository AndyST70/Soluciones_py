#16. Elabore un programa que permita ingresar un número de 3 dígitos y posteriormente lo desglose
#en decenas, centenas y unidades.

#* 892
#* 800
#* 90
#* 2

def desglose(num):
    centenas = num // 100   #845  -> 845/100 = 8
    decenas = (num % 100) // 10 # -> 45 % 100 = .45 /10 = 4  
    unidades = (num % 100) % 10 # -> 45 % 100 = .45 % 10 = 4.5 -> 5
    return centenas, decenas, unidades

def main():
    num = int(input("Ingrese un número de 3 dígitos: "))

    if num <= 100 or num <= 999:
        centenas, decenas, unidades = desglose(num)
        print(f"{centenas} centenas, {decenas} decenas, {unidades} unidades")
    else: 
        print("error me ingresaste un numero mayor a 3 digitiso")
if __name__ == "__main__":
    main()
