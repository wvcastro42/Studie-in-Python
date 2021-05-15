"""Des|empacotamento de argumentos."""

def meu_sum(*grupo_posicional, **grupo_nomeado):
    """Empacotamento."""
    print(grupo_posicional, grupo_nomeado)
    print(type(grupo_posicional), type(grupo_nomeado))
    return grupo_posicional, grupo_nomeado


lista = [1, 2, 3, 4]

def meu_mim(a, b, c, d, *args):
    """Desempacotamento."""
    return min((a, b, c, d, *args))

#Desempacotamento da lista dentro da função.
print(meu_max(*lista))


dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

def meu_max(a=0, b=0, c=0, d=0):
    return max((a, b, c, d))


# Desempacotamento do dicionário dentro da função
print(meu_max(**dicionario))
