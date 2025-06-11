def fact(n):
    if n == 0:
        # print(n)
        return 1
    else:
        print(f'{n}')
        return n * fact(n - 1)


print(fact(5))
