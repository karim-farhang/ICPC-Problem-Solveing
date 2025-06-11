from collections import Counter

a = 'abaca'
b = 'cdbda'

if Counter(a) == Counter(b) or len(a) == len(b):
    print('YES')
if len(a) != len(b):
    print("NO")
