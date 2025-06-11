import itertools
s = input()
li = list(itertools.permutations(s))
for i in li:
    print(*i)