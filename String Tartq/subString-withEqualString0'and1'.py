# -- sub string with equal string 0-1 --
s = input()
li = []
for i in range(len(s) + 1):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if len(sub) % 2 == 0:
            s1 = sub[:len(sub) // 2]
            s2 = sub[len(sub) // 2:]
            countz = s1.count('0')
            countone = s2.count('1')
            if len(sub) % 2 == 0 and countz == len(s1) and countone == len(s2):
                li.append(sub)
mx = 0
for i in li:
    if len(i) > mx:
        mx = len(i)
print(mx)
