# ----- longest suffix and prefix ------
s = input()
n = len(s)
b = False
for res in range(n // 2, 0, -1):
    prefix = s[0: res]
    suffix = s[n - res: n]
    if prefix == suffix:
        b=True
        print(res)
if not(b):
    print(0)
