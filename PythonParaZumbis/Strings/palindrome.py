''' Verifica se uma palavra é palindrome'''

palavra = input('Digite uma palavra: ')
is_palindrome = palavra == palavra[::-1]
print(f'NÃO é palíndrome!' if (is_palindrome) == False else 'É palindrome!')
