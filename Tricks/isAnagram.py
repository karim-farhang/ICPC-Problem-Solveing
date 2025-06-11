from collections import Counter


def isAnagram_N_Log_N(st1, st2):
    return sorted(st1) == sorted(st2)


def isAnagram_O_N(st1, st2):
    return Counter(st1) == Counter(st2)


print(isAnagram_O_N("listn", "silnt"))
print(isAnagram_N_Log_N("listn", "silnt"))
