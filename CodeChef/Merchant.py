"""
3
1000 3 0.25
3 200 0.1
0 100 0.2
"""

t = int(input())
rt = []
while t > 0:
    inp = input().split(' ')
    amount, price, tax = int(inp[0]), int(inp[1]), float(inp[2])
    muf = 0
    maf = ((amount * price) * tax) / 100
    rt.append(muf)
    t -= 1
print()
for i in rt:
    print(i)
