from math import prod

num_usados = []

class Operacoes:
    def soma ():
        cont = 0
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para somar: '))
            num_usados.insert(cont, n1)
            cont += 1
            
        soma_final = sum(num_usados)

        for i in num_usados:
            print(i)
        
        print('----- +')
        print(soma_final)

    def subtracao ():
        cont = 0
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para subtrair: '))
            num_usados.insert(cont, n1)
            cont += 1
        
        sub_final = num_usados[0]

        for i in num_usados[1:]:
            sub_final -= i

        for i in num_usados:
            print(i)
        
        print('_______ - ')
        print(sub_final)

    def multiplicacao ():
        cont = 0
        mult_final = 1
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para multiplicar: '))
            num_usados.insert(cont, n1)
            cont += 1

        mult_final = prod(num_usados)       

        for i in num_usados:
            print(i)
        
        print('_______ * ')
        print(mult_final)

    def potencia ():
        num_base = float(input('Digite o número para ser a base da potência: '))
        num_expo = float(input('Digite o número para ser o expoente da potência: '))
        potencia_final = num_base ** num_expo

        print(f'{num_base} ^ {num_expo} = {potencia_final}')

    def divisao ():
        cont = 0
        div_final = 1
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para dividir: '))

            if n1 == 0:
                print('Você não pode dividir por zero, digite um número válido!')
            
            else:
                num_usados.insert(cont, n1)
                cont += 1
        
        div_final = num_usados[0]

        for i in num_usados[1:]:
            div_final /= i

        for i in num_usados:
            print(i)
        
        print('_______ / ')
        print(div_final)

    def inteira (): 
        cont = 0
        div_final_inteiro = 1
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para dividir: '))

            if n1 == 0:
                print('Você não pode dividir por zero, digite um número válido!')
            
            else:
                num_usados.insert(cont, n1)
                cont += 1

        div_final_inteiro = num_usados[0]

        for i in num_usados[1:]:
            div_final_inteiro = div_final_inteiro // i

        for i in num_usados:
            print(i)
        
        print('_______ // ')
        print(div_final_inteiro)
        

    def resto (): 
        cont = 0
        div_final_resto = 1
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para dividir: '))

            if n1 == 0:
                print('Você não pode dividir por zero, digite um número válido!')
            
            else:
                num_usados.insert(cont, n1)
                cont += 1

        div_final_resto = num_usados[0]

        for i in num_usados[1:]:
            div_final_resto /= i

        for i in num_usados:
            print(i)
        
        print('_______ % ')
        print(div_final_resto)

