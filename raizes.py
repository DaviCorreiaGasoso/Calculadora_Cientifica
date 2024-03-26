import math

class Raiz_Quadrada:
    def __init__ (self, radicando):
        self.radicando = radicando

    def calculo_raiz (self):
        resultado = math.sqrt(self.radicando)
        print('O resultado da operação é {:.2f}'.format(resultado))

class Raizes:
    def __init__(self, rad, indice):
        self.rad = rad
        self.indice = indice
      
    def calculo_raizes(self):
        valor_final = pow(self.rad, (1/self.indice))
        print('O valor da operação é {:.2f}'.format(valor_final))