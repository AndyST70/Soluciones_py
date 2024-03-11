#19. Considere el siguiente proceso repetitivo para un número entero dado:
#Si el número es 1 el proceso termina. De lo contrario, si es par se divide entre 2, y si es impar se
#multiplica por 3 y se le suma 1.
#Si empezamos con 6, por ejemplo, obtendremos la sucesión de números 6, 3, 10, 5, 16, 8, 4, 2, 1.
#La conjetura de Collatz dice que, a partir de cualquier número inicial, la sucesión obtenida
#siempre termina en 1.
#Escriba un programa que permita verificar la conjetura de Collatz para cualquier entero dado, y
#que imprima la secuencia correspondiente.
#Ciclo 2024


#? si es numero par se divide entre 2
#? si es impar = (n*3) +1


def main():
    print("Ejercicio 19")
    numero = int(input("Ingrese un numero: "))
    numeor_collatz = collatz(numero)
    print(f"Secuencia de Collatz: {numeor_collatz}")
    print(*numeor_collatz, sep="->")
def collatz(numero):
    secuencia  = [numero]
    print(f"Secuencia: {secuencia}")
    while numero != 1: 
        #20 = 20/2 = 10     19/2 = 9.5
        if numero % 2 ==0: #si es el numero es par, y si no tenemos nada en residuo asumimos que es par
            numero = numero // 2
        else :
            numero = (numero * 3) + 1
        secuencia.append(numero)

    return secuencia





if __name__ == "__main__":
    main()