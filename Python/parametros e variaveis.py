def soma(*args): #*args aceita vários parametros por justaposição, criando uma tupla
    aux = 0
    for valor in args:
        aux += valor
    return aux

print('Print soma: ',soma(2,3,1,13))


def f(*args, **kwargs): #**kwargs aceita vários parametros por nome:valor, criando um dicionário
    print(args)
    print(kwargs)

print('\nPrint Tupla e dicionário')
f(1,2,3,75, nome = "Weverton", sobrenome = "Vasconcelos")


args = (1, 13, 666)
kwargs = {'cor':'azul', 'idade':35}

print("\nPrint desempacotando tupla e dicionário")
f(*args, **kwargs) #para receber uma variável e desempacotá-la deve-se usar * para tuplas e ** para dicionários
