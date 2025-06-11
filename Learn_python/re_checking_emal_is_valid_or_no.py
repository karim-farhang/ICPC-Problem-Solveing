import re

"""
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
email = input()
if re.search(pattern, email):
    print('valid email')
else:
    print('invalid email')
"""

pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3"
user_input = input()
new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)
