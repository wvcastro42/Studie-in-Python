''' Verifica se uma palavra é palindrome
palavra = input('Digite uma palavra: ')
is_palindrome = palavra == palavra[::-1]
print(f'NÃO é palíndrome!' if (is_palindrome) == False else 'É palindrome!')
'''

'''troca vogais por "*" '''
palavra = input('Palavra: ')
k = 0
troca = ''
while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[k]
    k += 1
print(troca)
