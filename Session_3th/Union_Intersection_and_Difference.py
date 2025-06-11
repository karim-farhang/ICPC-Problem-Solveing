Tc = int(input())
result = []
for i in range(Tc):
    set1 = set(input().split(","))
    set2 = set(input().split(","))
    u = set1.union(set2)
    intr = set1.intersection(set2)
    defr = set1.difference(set2)

    result.append(u)
    result.append(intr)
    result.append(defr)

print()
for i in range(len(result)):
    for j in range(len(result[i])):
        print(j,end=" ")
    print()