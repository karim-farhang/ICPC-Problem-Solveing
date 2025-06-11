def swapCount(s):
    swap = 0
    imbalance = 0;
    for i in s:
        if i == '[':
            imbalance -= 1
        else:
            imbalance += 1
            if imbalance > 0:
                swap += imbalance
    return swap
s = "[]][][";
print(swapCount(s))
s = "[[][]]";
print(swapCount(s))