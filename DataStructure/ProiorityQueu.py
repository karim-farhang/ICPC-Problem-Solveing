import queue
import random

proq = queue.PriorityQueue()
for i in range(10):
    proq.put(random.randrange(1, 100))

for j in range(proq.qsize()):
    print(proq.get())
