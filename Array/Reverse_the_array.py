a = [1, 2, 3, 4, 5]


def rotate(arr, n):
    b = [arr[-1]]
    for i in arr:
        b.append(i)
    return b[0:-1]


print(* rotate(a, len(a)))
