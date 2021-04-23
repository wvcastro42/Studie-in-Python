"""Teste para os exercícios do Python Para Zumbis."""


# B. x_antes
# Dada uma lista de strings retorna uma lista onde
# todos os elementos que começam com x ficam sorteados antes
# Ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: monte duas listas separadas e junte-as no final
def x_antes(words):
    new_list_x = []
    end_list = []
    for i in words:
        if i[0].lower() == 'x':
            print(i)
            new_list_x.append(i)
        else:
            end_list.append(i)
    new_list_x.extend(end_list)
    return new_list_x

print(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
