# -- caesar cipher ----
n = int(input())
st = input()
d = int(input())
for i in st:
    if i.isalpha():
        index = ord(i)
        d = d % 26
        index += d
        if i.islower() and index > 122:
            index -= 26
            print(chr(index), end="")
        elif i.islower():
            print(chr(index), end="")
        elif i.isupper() and index > 90:
            index -= 26
            print(chr(index), end="")
        elif i.isupper():
            print(chr(index), end="")
    else:
        print(i, end="")
