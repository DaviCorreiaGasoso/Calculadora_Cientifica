import math

class pi:
    def __init__(self):
        pass

    def calculo_area (self):
        raio = float (input("Digite o valor do raio: "))
        area = math.pi * math.pow (raio, 2) 
        print ("O valor da área é {:.2f}".format(area))
    
    def calculo_circunferencia(self):
        raio = float (input ("Digite o valor da raio: "))
        circuferencia = 2 * math.pi * raio
        print ("A circunferencia do raio é: " , circuferencia)
