def convert_num(x: int) -> int:
    str_x = str(x)[::-1]
    int_x = int(str_x)
    n_zeros = len(str_x) - len(str(int_x))
    return n_zeros

print(convert_num(1000))
