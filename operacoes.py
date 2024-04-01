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
        return soma_final

    def subtracao ():
        cont = 0
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para subtrair: '))
            num_usados.insert(cont, n1)
            cont += 1
            soma_final = sum(num_usados)

            for i in num_usados:
                sub_final = soma_final - i

        return sub_final

    def multiplicacao ():
        cont = 0
        mult_final = 1
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para multiplicar: '))
            num_usados.insert(cont, n1)
            cont += 1

        mult_final = prod(num_usados)       
        return mult_final

    def potencia ():
        num_base = float(input('Digite o número para ser a base da potência: '))
        num_expo = float(input('Digite o número para ser o expoente da potência: '))
        potencia_final = num_base ** num_expo 

        return potencia_final

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

            for i in num_usados:
                div_final = i / div_final
        
        return div_final

    def resto (a , b): 
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

            for i in num_usados:
                div_final_resto = i % div_final_resto
        
        return div_final_resto

    def inteira (): 
        cont = 0
        div_final_inteira = 1
        quant = float(input('Digite quantos números que você deseja operar: '))

        while cont < quant:
            n1 = float(input('Digite o número para dividir: '))

            if n1 == 0:
                print('Você não pode dividir por zero, digite um número válido!')
            
            else:
                num_usados.insert(cont, n1)
                cont += 1

            for i in num_usados:
                div_final_inteira = i // div_final_inteira
        
        return div_final_inteira
