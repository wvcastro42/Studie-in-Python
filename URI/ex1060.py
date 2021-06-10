num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())

list_nums = list((num1, num2, num3, num4, num5, num6))

print(f'{len([num for num in list_nums if num > 0])} valores positivos')
