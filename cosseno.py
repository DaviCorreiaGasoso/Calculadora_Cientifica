#Esse foi feito por Brenda! 

import math
class Cosseno:
    def cosseno():
        angulo_grau = float(input("Digite o ângulo em graus: "))
        angulo_radiano = math.radians(angulo_grau)
        cosseno_angulo = math.cos(angulo_radiano)

        print("O Cosseno de ", angulo_grau, " graus é: ", cosseno_angulo)