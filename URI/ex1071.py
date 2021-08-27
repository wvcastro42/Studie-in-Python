n1 = int(input())
n2 = int(input())
count = 0
if n1 % n2 != 0:
    n1, n2 = n2, n1

for num in list(range(n1+1, n2)):
    if num%2 == 1:
        count += num

print(count)
