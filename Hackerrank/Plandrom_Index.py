# ------- palindrome index ------------
def palindromeIndex(s):
    s = list(s)
    l, r = 0, len(s) - 1
    for i in range(len(s) // 2):
        if s[l] != s[r]:
            s.pop(l)
            if s == s[::-1]:
                return l
            else:
                return r
        l += 1
        r -= 1
    return -1


t = int(input())
res = []
while t > 0:
    st = list(input())
    print(palindromeIndex(st))
    t -= 1
