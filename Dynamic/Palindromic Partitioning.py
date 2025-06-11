# -------- Palindromic Partitioning --------------
# Given a string str,a partitioning of the string is a palindrome
# partitioning if every sub-string of the partition is a palindrome.
# Determine the fewest cuts needed for palindrome partitioning of the
# given string
# Input: str = "ababbbabbababa"
# Output: 3
# After 3 partitioning substrings
# are "a", "babbbab", "b", "ababa".

def palindromicPartition(s):
    n = len(s)
    C = [0] * n
    P = [[False for i in range(n)] for i in range(n)]
    for i in range(n):
        P[i][i] = True
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if L == 2:
                P[i][j] = (s[i] == s[j])
            else:
                P[i][j] = ((s[i] == s[j]) & P[i + 1][j - 1])
    for i in range(n):
        if P[0][i]:
            C[i] = 0
        else:
            C[i] = (1 << 32)
            for j in range(i):
                if P[j + 1][i] == True and C[j] + 1 < C[i]:
                    C[i] = C[j] + 1
    return C[n - 1]
print(palindromicPartition('ababbbabbababa'))
