#Esse foi feito pelo gatinho do Dayvsson
import math

angulo_grau = float(input("Digite o ângulo em graus: "))

angulo_radiano = math.radians(angulo_grau)

tangente_angulo= math.tan(angulo_radiano)

print("o cosseno de", angulo_grau,  "graus é: ", tangente_angulo)
