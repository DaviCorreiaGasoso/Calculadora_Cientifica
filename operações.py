def lista (self):
    i = 0
    num_usados = [] 
    while i <= (self - 1):
        n1 = float(input('Digite o número para operar: '))
        num_usados.insert(i, n1)
        i += 1  

def soma (self):
    somafinal = sum(lista())
    print(somafinal)

def subtracao (self):
    i = 0
    con = 0
    num_usados = [] 
    while i <= (self - 1):
        n1 = float(input('Digite o número para operar: '))
        num_usados.insert(i, n1)
        i += 1 
        somafinal = sum(num_usados)

        while con <= (self-1):
            subfinal = somafinal - num_usados[con]
            con += 1
    
    print(subfinal)


def multiplicacao (a , b): 
    return a * b 

def divisao (a , b): 
    if a or b == 0:
        return a / b 
    else: 
        return "Erro: divisão por zero!"

def potencia (a , b):
    return a ** b 

def resto (a , b):
    return a % b 

def inteira (a , b):
    return a // b