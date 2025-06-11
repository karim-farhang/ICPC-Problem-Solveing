from collections import Counter


# check is Palindrome or no
def isPalindrome(s):
    return s == s[::-1]


# check is Anagram or no
def isAnagram(s1, s2):
    return Counter(s1) == Counter(s2)


# sort by max length
a = "Hi Karim Welcome to python Trick".split()
a.sort(key=len, reverse=True)
print(a)

# sort by frequency
s = 'programmingknowlege'
sf = Counter(s)
print(sf)
Atem = list(sf.items())

Atem.sort(key=lambda x: x[1])
print(Atem)
print(lambda x: [x[1], x[0]])
Atem.sort(key=lambda x: [x[1], x[0]])
print(Atem)
