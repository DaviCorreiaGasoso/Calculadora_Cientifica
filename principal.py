from pi import Pi
from operacoes import Operacoes
import cosseno
import seno
import raizes
import tangente
    
print("Bem vindo à calculadora cientifica!")
print("1. Raiz quadrada")
print("2. Pi")
print("3. Seno")
print("4. Cosseno")
print("5. Tangente")
print("6. Operações")
escolha = input("Escolha alguma operação (1/2/3/4/5/6): ")
num1 = float (input ("Escolha o numero1: "))
num2 = float (input ("Escolha o numero2: "))

if escolha == '1':
    print ("resultado: ", modulo_math.raizes (num1 , num2 ))
elif escolha == '2': 
    print ("resultado: ", modulo_math.pi (num1 , num2))
elif escolha == '3':
    print ("resultado: ", modulo_math.ceno (num1 , num2))
elif escolha == '4': 
    print ("resultado: ", modulo_math.cosseno (num1 , num2))
elif escolha == '5':
    print ("resultado: ", modulo_math.tangente (num1 , num2))
elif escolha == '6':
    print ("resultado: ", modulo_math.operacoes (num1 , num2))            
else: 
    print ("Opção Invalida!")