#Esse foi feito por Dayvsson e Isabele V.
import math
class Tangente:
    def tangente():
        angulo_grau = float(input("Digite o ângulo em graus: "))
        angulo_radiano = math.radians(angulo_grau)
        tangente_angulo= math.tan(angulo_radiano)
        print("O Cosseno de ", angulo_grau,  " é: ", tangente_angulo)
