s = input()
max = 0
max_s = ""
for i in range(len(s)+1):
    for j in range(i+1,len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1] and len(sub) > max:
            max = len(sub)
            max_s = sub
print(max_s)
            