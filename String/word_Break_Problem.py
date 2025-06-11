def wordBreak(words, word, out=''):
    if not word:
        print(out)
        return
    for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix in words:
            wordBreak(words, word[i:], out + '' + prefix)
ar = list(map(str,input().split(',')))
word = input()
wordBreak(ar, word)