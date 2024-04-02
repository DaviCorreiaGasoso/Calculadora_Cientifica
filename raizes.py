import math

class Raiz_Quadrada:
    def calculo_raiz (self):
        radicando = float(input('Digite o radicando: '))
        resultado = math.sqrt(self.radicando)
    
        print(f'√{radicando} = {resultado}')

class Raizes: 
    def calculo_raizes():
        rad = float(input('Digite o radicando: '))
        indice = float(input('Digite o índice: '))
        valor_final = pow(rad, (1/indice))

        print(f'{indice}√{rad} = {valor_final}')
        