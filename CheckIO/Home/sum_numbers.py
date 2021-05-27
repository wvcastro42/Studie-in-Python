from math import fsum
"""
return 0 + sum([int(word) for word in text.split(' ') if word.isnumeric()])
"""
"""
                        def sum_numbers(text):
                            tot=0
                            for word in text.split():
                                if word.isnumeric():
                                    tot += int(word)
                            return tot
"""
def sum_numbers(text: str) -> int:

    lista = text.split()
    lista_nums = []

    for i in lista:
        if i[0] in '0123456789' and i[-1] in '0123456789':
            lista_nums.append(float(i))


    if len(lista_nums) == 0:
        return 0

    elif len(lista_nums) == 1:
        return lista_nums[0]

    else:
        return int(fsum(lista_nums))




if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
