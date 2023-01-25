from sys import stdin

n = int(stdin.readline().strip())
nodes = list()

for _ in range(n):
    message = stdin.readline().strip().split()
    command = message[0].strip().lower()

    if len(message) > 1:
        num = int(message[1])

        if command == 'push':
            nodes.append(num)

    elif command == 'pop':
        print(nodes.pop(0)) if len(nodes) > 0 else print(-1)

    elif command == 'size':
        print(len(nodes))

    elif command == 'empty':
        if len(nodes) == 0:
            print(1)

        else:
            print(0)

    elif command == 'front':
        print(nodes[0]) if len(nodes) > 0 else print(-1)

    elif command == 'back':
        print(nodes[-1]) if len(nodes) > 0 else print(-1)
