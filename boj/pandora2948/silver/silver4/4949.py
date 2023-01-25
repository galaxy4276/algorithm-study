from sys import stdin

while True:
    msg = stdin.readline()
    if msg == '.\n':
        break
    stack = list()
    integrity = True
    try:
        for char in msg:
            if char == '.':
                break

            if char == '[':
                stack.append('[')

            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()

                else:
                    integrity = False
                    break

            elif char == '(':
                stack.append('(')

            elif char == ')':
                if stack[-1] == '(':
                    stack.pop()

                else:
                    integrity = False
                    break

        if not stack and integrity:
            print('yes')

        else:
            print('no')

    except IndexError:
        print('no')

