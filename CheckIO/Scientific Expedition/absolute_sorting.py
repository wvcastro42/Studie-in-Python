def checkio(values: list) -> list:

    # return sorted(values, key=abs)
    result = []

    for value in values:
        if abs(min(values)) == abs(value):
            result.append(value)
            values.remove(value)
        else:
            continue
    return result


if __name__ == '__main__':
    print("Example:")
    print(checkio([-20, -5, 10, 15]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
    assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
    assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
    print("Coding complete? Click 'Check' to earn cool rewards!")
