t = int(input())
rt = list()
while t > 0:
    incode = list(input())
    decode = list()
    element = incode.pop()
    decode.append(element)
    while incode != []:
        decode = decode[:len(decode)//2] + list(element) + decode[len(decode)//2:]
        element = incode.pop()
    print("".join(decode))
    t-=1
