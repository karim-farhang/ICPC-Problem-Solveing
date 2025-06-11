import re

s2 = 'This is a string with numbers in it: 1, 100, 2, 3, 4,99'
numbered = re.findall(r'(?:^|\b)([0-9]+)(?:\b)', s2)

print(numbered)
