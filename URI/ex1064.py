nums = []
i = 0
while i < 6:
    nums.append(float(input()))
    i += 1

count = 0
positives = 0

for num in nums:
    if num >= 0:
        positives += num
        count += 1

print(f'{count} valores positivos')
print(f'{positives/count:.1f}')
