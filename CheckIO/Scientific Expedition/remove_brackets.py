from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        print (s)
        return s
    else:
        print (s)
        return s

print(parChecker('((()))'))
print(parChecker('(()'))

# def remove_brackets(line: str) -> str:


# print(remove_brackets('[[(}]]'))

# if __name__ == '__main__':
#     print("Example:")
#     print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert remove_brackets('(()()') == '()()'
    # assert remove_brackets('[][[[') == '[]'
    # assert remove_brackets('[[(}]]') == '[[]]'
    # assert remove_brackets('[[{}()]]') == '[[{}()]]'
    # assert remove_brackets('[[[[[[') == ''
    # assert remove_brackets('[[[[}') == ''
    # assert remove_brackets('') == ''
    # assert remove_brackets('[(])') == '()'
    # print("Coding complete? Click 'Check' to earn cool rewards!")
