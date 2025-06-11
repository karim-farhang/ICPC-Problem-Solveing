st = input()
li = list()
if len(st) % 2 != 0:
    print("NO")
else:
    b = True
    for i in st:
        if i == "{" or i == "[" or i == "(":
            li.append(i)
        elif i == "}" or i == "]" or i == ")":
            if i == ")" and li.pop() != "(":
                b=False
                break
            elif i == "]" and li.pop() != "[":
                b=False
                break
            elif i == "}" and li.pop() != "{":
                b=False
                break
    if b:
        print("YES")
    else:
        print("NO")