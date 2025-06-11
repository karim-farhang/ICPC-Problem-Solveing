t = int(input().strip())
tr = []
start = "/----------\\"
tr.append(start)
end = "\\----------/"
while t > 0:
    st = '\\*!'
    en = '!*/'
    msg = input().strip()
    b_msg = st+msg+en
    tr.append(b_msg)
    t -= 1

tr.append(end)
for i in tr:
    print(i)