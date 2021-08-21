from typing import List


def letter_queue(commands: List[str]) -> str:

    queue = []
    for command in commands:

        if command == 'POP':
            if queue: queue.pop(0)

        else:
            queue.append(command[-1]) # or   queue.append(command.replace('PUSH ', ''))

    return(''.join(queue))

    # result = []
    # i = 0
    # while i < len(commands):
    #
    #     if commands[i][0:5] == 'PUSH ':
    #         result.append(commands[i][5])
    #
    #     if commands[i][0:3] == 'POP':
    #         if result == []:
    #             pass
    #         else:
    #             result.pop(0)
    #
    #     i += 1
    #
    # return ''.join(result)

if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',      #0
        'POP',      #1
        'PUSH Z',   #2
        'PUSH D',   #3
        'PUSH O',   #4
        'POP',      #5
        'PUSH T'])) #6

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
