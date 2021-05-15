def convert_num(x: int) -> int:
    str_x = str(x)[::-1]
    int_x = int(str_x)
    n_zeros = len(str_x) - len(str(int_x))
    return n_zeros



def end_zeros(num: int) -> int:
    return convert_num(num)


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
