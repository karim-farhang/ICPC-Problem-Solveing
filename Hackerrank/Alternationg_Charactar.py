# -- alternating character ----
t = int(input())
while t > 0:
    st = list(input())
    for i in range(len(st) - 1):
        if st[i] == 'A' and st[i + 1] != 'B' or st[i] == 'B' and st[i + 1] != 'A':
            st[i] = ' '
    print(st.count(' '))
    t -= 1
