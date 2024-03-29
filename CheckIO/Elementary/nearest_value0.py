def nearest_value(values: set, one: int) -> int:

    if one in values:
        return one

    lista = list(values)
    lista.append(one)
    lista.sort()
    idx_one = lista.index(one)

    if idx_one == 0 or idx_one == len(lista)-1:
        return lista[1] if idx_one == 0 else lista[-2]

    else:
        if (one - lista[idx_one - 1]) <= (lista[idx_one + 1] - one):
            return lista[idx_one - 1]
        return lista[idx_one + 1]



if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
