from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:

    f, b, l, r = (instructions.count(d) for d in 'fblr')
    return r-l, f-b

    # movies = {'f': 1, 'b': -1, 'r': 1, 'l': -1}
    # forwardback = 0
    # rightleft = 0
    #
    # for step in instructions:
    #
    #     if step == 'f' or step == 'b':
    #         forwardback += movies[step]
    #     else:
    #         rightleft += movies[step]
    #
    # return (rightleft, forwardback)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
