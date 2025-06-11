tc = int(input())
Re = []
while tc > 0:
    w = int(input())
    words = input().split(" ")
    x = str()
    for i in range(w):
        x += str(words[i])
    print(len(set(x)))
    tc -= 1
