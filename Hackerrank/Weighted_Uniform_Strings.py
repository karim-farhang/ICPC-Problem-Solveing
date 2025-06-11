# -- weighted uniform string -----
s = input()
t = int(input())
w = 0
dic = {}
for i in range(0, len(s)):
    if i == 0 or s[i] != s[i - 1]:
        w = ord(s[i]) - ord('a') + 1
    else:
        w = w + ord(s[i]) - ord('a') + 1
    dic[w] = 1
for i in range(t):
    x = int(input())
    print('Yes' if x in dic else 'No')
