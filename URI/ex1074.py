n = int(input())
i = 0
numbers = []

while i < n:
    numbers.append(int(input()))
    i += 1

for num in numbers:

    if num == 0:
        print('NULL')

    elif num < 0:
        if num%2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')

    else:
        if num%2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
