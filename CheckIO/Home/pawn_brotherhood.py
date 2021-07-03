def safe_pawns(pawns: set) -> int:
    num = 0
    for i in pawns:
        left = chr(ord(list(i)[0])-1) + chr(ord(list(i)[1])-1)
        right = chr(ord(list(i)[0])+1) + chr(ord(list(i)[1])-1)

        if left in pawns or right in pawns:
            num += 1

    return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
