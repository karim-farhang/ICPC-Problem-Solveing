tc = int(input())
rtc = []
while tc > 0:
    st = list(input())
    st.sort(key=lambda x: st.count(x),reverse=True)
    print(st)
    tc -= 1
