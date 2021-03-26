def fat(n):
    f = 1
    while n > 0:
        f = f * n
        n -= 1
    return f

print(fat(3))
print(fat(5))
for i in range(6): print(fat(i))
