from collections import deque

x = deque(deque())
x.append(deque([1, 2, 3, ]))
x.append(deque([1, 2, 4, ]))
x.append(deque([1, 2, 7, ]))
x.rotate(-2)
for i in x:
    print(i)
