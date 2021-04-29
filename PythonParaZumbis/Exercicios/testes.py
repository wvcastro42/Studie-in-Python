"""Teste para os exercícios do Python Para Zumbis."""


# C. sort_last
# Dada uma lista de tuplas não vazias retorna uma tupla ordenada
# por ordem crescente do último elemento
# Exemplo [(1, 7), (1, 3), (3, 4, 5), (2, 2)] retorna
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use key=função que você definiu e que retorna o último elemento
def sort_last(tuples):
    new_list_x = []
    for index_t, element_t in enumerate(tuples):
        print(f'atual: {element_t[-1]}')
        print(f'próximo: {tuples[index_t+1][-1]}\n')
        # break
    return 0


x = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sort_last(x))
