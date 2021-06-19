from collections import Counter

def frequency_sort(items):

    return [numero for numeros, count in Counter(items).most_common() for numero in [numeros] * count]

    # new_list = []
    # common = Counter(items).most_common()
    #
    # for idx, elem in enumerate(common):
    #
    #     count = 0
    #     while count < common[idx][1]:
    #         new_list.append(common[idx][0])
    #         count += 1
    #
    # return new_list


print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))  # [4, 4, 4, 4, 6, 6, 2, 2]

# if __name__ == '__main__':
#     print("Example:")
#     print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
#     assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
#     assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
#     assert list(frequency_sort([])) == []
#     assert list(frequency_sort([1])) == [1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
