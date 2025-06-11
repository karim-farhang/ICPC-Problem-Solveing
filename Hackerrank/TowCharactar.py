# --- tow character ----------
n = int(input())
st = input()
st = list(st)
while True:
    element = ""
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            element = st[i]
    i = 0
    while i < len(st):
        if st[i] == element:
            st.remove(st[i])
        i += 1
    b = False
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            b = True
    if not (b):
        break
print(st)
