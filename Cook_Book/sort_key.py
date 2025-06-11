import operator
import unicodedata
import textwrap
import string

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 50))
print(textwrap.fill(s, 50, initial_indent='      ', subsequent_indent='       '))

name = 'Guido'
n = 37

s = string.Template('$name has $n messages.')
print(s.substitute(vars()))

