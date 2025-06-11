d = int(input())
r = 5
res = 0
for _ in range(d):
    like = r // 2
    res += like
    r = like * 3
print(res)
