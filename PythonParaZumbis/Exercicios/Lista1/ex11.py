'''
Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
'''
qtde_digitos = len(str(2**1_000_000))

print(f'2 ** 1_000_000 tem {qtde_digitos} de dígitos')
