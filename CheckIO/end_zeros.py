def convert_num(num: int) -> int:
    if num == 0:
        return 1
    int_num = int(str(num)[::-1])
    n_zeros = len(str(num)) - len(str(int_num))
    return n_zeros

print(convert_num(1001))
