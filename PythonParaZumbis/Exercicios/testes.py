"""Teste para os exercícios do Python Para Zumbis."""


  # test(has22([1, 2, 2]), True)
  # test(has22([1, 2, 1, 2]), False)
 # Ainda não obtido: False esperado: True
 # Ainda não obtido: True esperado: False

# K. has22 #
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False
def has22(nums):
    for i in range(len(nums)-1):
        # print(i)
        if nums[i] == 2:
            # print(i)
            if nums[i+1] == 2:
                return True
    return False

lista = [1, 2, 2]

print(has22(lista))
