print("Please Enter the Number with base (Ob,Oo,Ox):")
x = input()
base, num = x[0:2], x[2:len(x)]
if base == 'Ob':
    num = int(num, base=2)
if base == 'Oo':
    num = int(num, base=8)
if base == 'Ox':
    num = int(num, base=16)
print("Please Enter the base (bin,oct,dec,hex):")
y = str(input())
if y.lower() == 'bin':
    print(bin(num)[2:])
if y.lower() == 'oct':
    print(oct(num)[2:])
if y.lower() == 'dec':
    print(int(num))
if y.lower() == 'hex':
    print(hex(num)[2:])
