"""
3
Redivide
please do not step on the pets there.
The owl Ate my metal worm
----------------------------
1
15
7
"""
t = int(input())
rtc = []
while t > 0:
    sentence = input()
    sentence = list(sentence.replace(' ', ''))
    sentence.sort()
    remove = 0
    flag = False
    counter = 0
    for i in sentence:
        c = sentence.count(i)
        if c % 2 == 1 and flag == False:
            flag = True
        elif c % 2 == 1:
            counter += 1
            sentence.remove(i)

    flag = False
    for i in sentence:
        c = sentence.count(i)
        if c % 2 == 1 and flag == False:
            flag = True
        elif c % 2 == 1:
            counter += 1
            sentence.remove(i)
    rtc.append(counter)
    print(*sentence)
    t -= 1
for j in rtc:
    print(j)
