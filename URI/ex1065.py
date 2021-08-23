nums = []
i = 0
while i < 5:
    nums.append(int(input()))
    i += 1

evens = 0
for num in nums:
    if num % 2 == 0:
        evens += 1

print(f'{evens} valores pares')
