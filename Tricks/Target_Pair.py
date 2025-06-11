def findTarget(A, K):
    st = set()
    for i in range(len(A)):
        complement = K - A[i]
        if complement in st:
            return [complement, A[i]]
        else:
            st.add(A[i])


A = [5, 100, 50, 10, 30, 5, 7, 85, 90, 100]
k = 17
x = findTarget(A, k)
print(x)
