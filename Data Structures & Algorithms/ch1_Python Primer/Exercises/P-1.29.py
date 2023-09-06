import itertools
characters = ['c', 'a', 't', 'd', 'o', 'g']

permutations = list(itertools.permutations(characters))

for permutate in permutations:
    print("".join(permutate))