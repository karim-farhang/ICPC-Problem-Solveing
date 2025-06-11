import string

"""
5
aaa hack zzz abcd szxp
"""
import string
def alic_message(siz, arr):
    if siz == 1:
        return 1
    if siz == 0:
        return 0
    else:
        a = list(string.ascii_lowercase)[::-1]
        decode = []
        for i in arr:
            x = []
            for j in i:
                if a.index(j) < len(a) / 2:
                    x.append(j)
            decode.append(x)
        while decode.count([]) > 1:
            decode.remove([])
        r = ''
        for i in decode:
            for j in i:
                r += j
        r = set(list(r))
        for i in r:
            if a.index(i) > len(a) / 2:
                r.remove(i)
        return len(r) - 1


siz = int(input())
alic_msg = input().split(' ')
print(alic_message(siz, alic_msg))
