import heapq

# heap is like binary tree root is small right is big left is big root small right
li = []
heapq.heappush(li, 10)
print(li)
heapq.heappush(li, 1)
print(li)
heapq.heappush(li, 5)
print(li)
heapq.heappush(li, 10)
print(li)
# heap pop is remove small element from list
x = heapq.heappop(li)
print(x)
# heap is one data structure for store data heapfiy() is a function make convert list to heap
heapq.heapify(li)
print(li)
x = heapq.heappushpop(li, 20)
print(x)
print(*li)
x = heapq.heapreplace(li, 100)
print(x)
print(*li)
x = heapq.nsmallest(2, li)
print(x)
x = heapq.nlargest(2, li)
print(x)
list2 = [(1, 'karim'), (2, 'farhang'), (4, 'ali'), (9, 'nasim'), (0, 'nabi')]
lisg = []
heapq.heapify(list2)
for i in range(len(list2)):
    lisg.append(heapq.heappop(list2))
print(lisg)
