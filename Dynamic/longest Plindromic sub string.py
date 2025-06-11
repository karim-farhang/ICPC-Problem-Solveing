# Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):
    if len(s) <= 1:
        return s
    start = end = 0
    length = len(s)
    for i in range(length):
        max_len_1 = get_max_len(s, i, i + 1)
        max_len_2 = get_max_len(s, i, i)
        max_len = max(max_len_1, max_len_2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start: end + 1]


def get_max_len(s, left, right):
    length = len(s)
    i = 1
    while left >= 0 and right < length and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


s = "babad"
print(longestPalindrome(s))
