# --- making anagram -------
a = input()
b = input()
buffer = [0] * 26
for char in a:
    buffer[ord(char) - ord('a')] += 1
for char in b:
    buffer[ord(char) - ord('a')] -= 1
print(sum(map(abs, buffer)))
