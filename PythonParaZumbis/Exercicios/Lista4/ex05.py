'''Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python”
e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas
para minúsculas e de remover antes os caracteres especiais.'''


lista = '''
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.”.
'''.lower()

import string

for c in string.punctuation:
    lista = lista.replace(c, ' ')

lista = lista.split()

def is_letra(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
        return False

# resp = []
#
# for p in lista:
#     if is_letra(p) and len(p) > 4:
#         resp.append(p)

''' With list comprehension '''
resp = [p for p in lista if is_letra(p) and len(p) > 4]

print(resp)
print(len(resp))



# Minha solução
# for i in lista.split():
#     if i in 'python':
#         soma = soma + 1
#         quatro_ou_mais = 0
#         while j < len(i):
#             if i[j] in 'python':
#                 quatro_ou_mais = quatro_ou_mais + 1
#             j += 1
#             if quatro_ou_mais >= 4:
#                 total += 1
# print(total)
# print(soma)
