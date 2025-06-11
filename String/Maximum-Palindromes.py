from collections import defaultdict
def sherlockAndAnagrams(s):
    n = len(s)
    out = 0
    hash_map = defaultdict(lambda:0)
    for i in range(n):
        for j in range(i+1, n+1):
            c = "".join(sorted(s[i:j]))
            out += hash_map[c]
            hash_map[c] += 1
    return out
s = input()
print(sherlockAndAnagrams(s))