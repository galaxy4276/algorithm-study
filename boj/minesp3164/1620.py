from sys import stdin


def input():
    return stdin.readline().rstrip()


pokemon_max, problem_n = map(int, input().split())
pokemon_name = {}
pokemon_id = {}
for i in range(pokemon_max):
    a = input()
    pokemon_name[i + 1] = a
    pokemon_id[a] = i + 1

for j in range(problem_n):
    problem = input()
    if problem.isdigit():
        print(pokemon_name[int(problem)])
    else:
        print(pokemon_id[problem])
