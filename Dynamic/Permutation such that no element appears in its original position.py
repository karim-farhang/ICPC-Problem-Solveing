# --- Count Derangement's ----
# (Permutation such that no element appears in its original position)
def countDer(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (n - 1) * (countDer(n - 1) + countDer(n - 2))
n = 4
print("Count of Derangement's is ", countDer(n))
