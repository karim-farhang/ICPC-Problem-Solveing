x = 'forgeeksskeegfor'
long = ''
for i in range(len(x)):
    for j in range(len(x)):
        if x[i:j] == x[i:j][::-1]:
            if len(x[i:j]) > len(long):
                long = x[i:j]

print(long)
