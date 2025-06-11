from collections import deque

x = deque()

list1 = [
    ['1', '2', '3', '+'],
    ['1', '2', '3', '7'],
    ['1', '2', '3', '6'],
    ['1', '2', '3', '5'],
    ['1', '2', '3', '4'],
]
x.extend(list1)
xr = deque()
for j in x:
    xr.append(j)
    xr.rotate(1)

 
for p in xr:
    print(p)

