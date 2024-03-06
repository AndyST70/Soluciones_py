#10. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos de un
#día desde las 0:00:00 horas hasta las 23:59:59 horas

import time 
import datetime
def main():
    #form1 
    # dat1 = time.localtime()
    # print("Hora actual: ", dat1.tm_hour, ":", dat1.tm_min, ":", dat1.tm_sec)
    # flag = True
    # while flag:
    #     dat1 = time.localtime()
    #     print("Hora actual: ", dat1.tm_hour, ":", dat1.tm_min, ":", dat1.tm_sec)
    #     time.sleep(1)
    #     if dat1.tm_hour == 23 and dat1.tm_min == 59 and dat1.tm_sec == 59:
    #         flag = False
    #         print("Fin del dia")
    #         break
    #     else:
    #         flag = True
    #         continue
    #form2
    print("Forma 2")
    for hora in range(24):
        for minuto in range(60):
             for segundo in range(60):
                 print(hora, ":", minuto, ":", segundo)
                 time.sleep(1)


if __name__ == "__main__":
    main()