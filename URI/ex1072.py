# n = int(input())
# i = 0
# numbers = []

# while i < n:
#     numbers.append(int(input()))
#     i += 1
#


nums = [list(int(x) for x in input().split()) for i in range(int(input()))]
in_range1020 = 0
out_range1020 = 0

for num in nums:
    if num[0] in range(10,21):
        in_range1020 += 1
    else:
        out_range1020 += 1

print(f'{in_range1020} in')
print(f'{out_range1020} out')
