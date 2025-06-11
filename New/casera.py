"""
7
encrypt 1 aaa
encrypt 1 zzz
encrypt 2 xyz
decrypt -27 aaa
decrypt -2 zbc
encrypt 26 vvv
decrypt -26 nnn

"""
t = int(input())
while t > 0:
    st, no, st1 = map(str, input().split(' '))
    no = int(no)
    if st == 'encrypt' and no > 0:
        for i in st1:
            num = ord(i) + no
            if num > 122:
                num %= 122
                print(chr(num + 96), end="")
            else:
                print(chr(num), end="")
    if st == "decrypt" and no < 0:
        for i in st1:
            neg = ord(i) + no
            if neg < 97:
                no *= -1
                no %= 26
                no *= -1
                sum = ord(i) + no
                print(chr(sum + 26), end="")
            else:
                print(chr(neg), end="")
    print()
    t -= 1
