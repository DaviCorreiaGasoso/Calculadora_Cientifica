#Esse codigo foi feito por Cesar! 
import math

angulos_graus = float(input("Digite qual oangulo vc deseja calcular: "))

angulos_radianos = math.radians(angulos_graus)

seno_angulo = math.sin(angulos_radianos)

print("O Seno de: ", angulos_graus, "graus é: ", seno_angulo)