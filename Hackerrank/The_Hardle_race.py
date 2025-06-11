n, k = map(int, input().split())
H_race = list(map(int, input().split()))
x = max(H_race)
if x > k:
    print(x - k)
else:
    print(0)
