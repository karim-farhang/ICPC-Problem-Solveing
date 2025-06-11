x = list(map(int, input().split()))
print(all([y for y in x if y % 2 == 0]))
