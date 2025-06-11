from collections import deque
def shortestChainLen(src, dist, words):
    if src == dist:
        return 0
    if dist not in words:
        return 0
    level, wordLength = 0, len(src)
    Q = deque()
    Q.append(src)
    while len(Q) > 0:
        level += 1
        sizeofQ = len(Q)
        for i in range(sizeofQ):
            word = [j for j in Q.popleft()]
            for pos in range(wordLength):
                orig_char = word[pos]
                for c in range(ord('a'), ord('z') + 1):
                    word[pos] = chr(c)
                    if "".join(word) == dist:
                        return level + 1
                    if "".join(word) not in words:
                        continue
                    del words["".join(word)]
                    Q.append("".join(word))
                word[pos] = orig_char
    return 0


words = {"poon": 1, "plee": 1, "same": 1, "poie": 1, "plie": 1, "poin": 1, "plea": 1, }
print(shortestChainLen('toon', 'plea', words))
