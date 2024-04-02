#Esse codigo foi feito por Cesar! 
import math
class Seno:
    def seno():
        angulos_graus = float(input("Digite qual o ângulo você deseja calcular: "))
        angulos_radianos = math.radians(angulos_graus)
        seno_angulo = math.sin(angulos_radianos)
        print("O Seno de: ", angulos_graus, " é: ", seno_angulo)
