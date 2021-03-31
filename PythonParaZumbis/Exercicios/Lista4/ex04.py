'''
Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''

lista = '''
The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principlesn. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.
'''.lower()
'''
import string
for c in string.punctuation:
    lista = lista.replace(c, ' ')

print(lista + '\n\n')

l_resutado = []

for i in lista.split():
    if i[0] in 'python' or i[-1] in 'python':
        l_resutado.append(i)

print(l_resutado)

'''

import string
for c in string.punctuation:
    lista = lista.replace(c, ' ')
resp = [p for p in lista.split()
        if p[0] in 'python' or p[-1] in 'python']
print(resp)
