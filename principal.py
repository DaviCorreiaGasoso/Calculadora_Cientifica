from pi import Pi
from operacoes import Operacoes
from raizes import Raiz_Quadrada, Raizes
from seno import Seno
from cosseno import Cosseno
from tangente import Tangente


print ('Calculadora Científica - BDDDGST')
print ('Você pode fazer as operações seguintes:')
print ('1- Soma \n2- Subtração \n3- Divisões \n4- Multiplicação \n5- Potência \n6- Pi \n7- Raiz \n8- Seno, Cosseno e Tangente \n')

while True:
    escolha = int(input('Digite o número da operação desejada: '))

    if escolha == 1:
        Operacoes.soma()
        break
    
    elif escolha == 2:
        Operacoes.subtracao()
        break

    elif escolha == 3:
        print('Dentro da nossa calculadora tem as seguintes divisões: ')
        print('Resto, Inteira e Normal\n')

        while True:
            acao = str(input('Digite o nome da operação da divisão desejada: '))

            if acao.capitalize() == 'Resto':
                Operacoes.resto()
                break

            elif acao.capitalize() == 'Inteira':
                Operacoes.inteira()
                break

            elif acao.capitalize() == 'Normal':
                Operacoes.divisao()
                break
            
            else:
                print('Escreva uma operação válida /n')
        break
    
    elif escolha == 4:
        Operacoes.multiplicacao()
        break

    elif escolha == 5:
        Operacoes.potencia()
        break
    elif escolha == 6:
        print('Dentro da nossa calculadora tem as seguintes operações com Pi: ')
        print('Área e Circuferência \n')

        while True:
            acao = str(input('Digite o nome da operação de Pi desejada: '))

            if acao.capitalize() == 'Área':
                Pi.calculo_area()
                break

            elif acao.title() == 'Circuferência':
                Pi.calculo_circunferencia()
                break
            
            else:
                print('Escreva uma operação válida /n')
        break

    
    elif escolha == 7:
        print('Dentro da nossa calculadora tem as seguintes raízes: ')
        print('Raiz Quadrada e Raiz \n')

        while True:
            acao = str(input('Digite o nome da operação da raiz desejada: '))

            if acao.capitalize() == 'Raiz':
                Raizes.calculo_raizes()
                break

            elif acao.title() == 'Raiz Quadrada':
                Raiz_Quadrada.calculo_raiz()
                break
            
            else:
                print('Escreva uma operação válida /n')
        break
    
    elif escolha == 8:
        while True:
            acao = str(input('Digite o nome da operação desejada: '))

            if acao.capitalize() == 'Seno':
                Seno.seno()
                break

            elif acao.title() == 'Cosseno':
                Cosseno.cosseno()
                break
            
            elif acao.title() == 'Tangente':
                Tangente.tangente()
                break
            
            else:
                print('Escreva uma operação válida /n')
        break
