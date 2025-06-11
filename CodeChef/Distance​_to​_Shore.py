import math


def PythagoreanTheorem(a=0.0, b=0.0, c=0.0):
    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)
    if a == 0:
        return math.sqrt(c - b)
    if b == 0:
        return math.sqrt(c - a)
    if c == 0:
        return math.sqrt(a + b)


t = int(input().strip())
rt = []
while t > 0:
    value = [x for x in input().strip().split(' ')]
    z1, v_z1, z2, v_z2 = value[0].lower(), float(value[1]), value[2].lower(), float(value[3])
    result = 0
    if z1 == 'a' and z2 == 'b':
        result = PythagoreanTheorem(v_z1, v_z2, 0)
    if z2 == 'a' and z1 == 'b':
        result = PythagoreanTheorem(v_z2, v_z1, 0)
    if z1 == 'c' and z2 == 'a':
        result = PythagoreanTheorem(v_z2, 0, v_z1)
    if z1 == 'a' and z2 == 'c':
        result = PythagoreanTheorem(v_z1, 0, v_z2)
    if z1 == 'b' and z2 == 'c':
        result = PythagoreanTheorem(0, v_z1, v_z2)
    if z1 == 'c' and z2 == 'b':
        result = PythagoreanTheorem(0, v_z2, v_z1)
    rt.append(int(result))
    t -= 1

for j in rt:
    print(j)
