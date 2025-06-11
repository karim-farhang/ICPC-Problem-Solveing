st = list(input().split(','))
k = int(input())
for i in range(k):
    st.append(st.pop(0))
print(st)
