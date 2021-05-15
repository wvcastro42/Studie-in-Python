"""Minissérie Pythonica: Funções #2 - Argumentos posicionais, nomeados e o Python 3.8."""

anonima = lambda param: param + 2
anonima_plus = lambda param1, param2: param1 + param2


def soma_posicional(x, y):
    """X e Y são parâmetros posicionais."""
    return x + y

def soma_explicitamente_nomeados(*, x=7, y=7): # o asterisco faz a função aceitar apenas argumentos nomeados
    """X e Y são parâmetros nomeados."""
    """Na falta de X ou Y o valor 7 será usado."""
    print(f'x: {x}\t y: {y}')
    return x + y
