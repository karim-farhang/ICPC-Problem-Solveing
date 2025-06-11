def Fibonace(n):
    x = 0
    if n == 0:
        return x
    else:
        x = Fibonace(n - 1) + Fibonace(n - 2)


print(Fibonace(20))
