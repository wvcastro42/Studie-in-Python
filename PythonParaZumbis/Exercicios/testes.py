nums = [5, 2, 3]
lista = []

if nums[0] > nums[-1]:
    for i in range(len(nums)):
        lista.append(nums[0])
else:
    for i in range(len(nums)):
        lista.append(nums[-1])

print(lista)
