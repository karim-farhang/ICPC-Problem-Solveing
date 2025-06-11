"""
5
affect effect
except accept
alternately alternatively
bare bear
censor sensor
4
The colors had a great affect on him, accept blue.
We alternatively took turns fighting the bare, bear handed.
China wants to sensor the affect of a bare in the cities.
The college will except me into their college, or alternately will reject me.
"""
import string

w = int(input())
wordA = []
wordB = []
for i in range(w):
    x, y = input().split(' ')
    wordA.append(x)
    wordB.append(y)

sen = int(input())
sentensce = []
for i in range(sen):
    sentensce.append(input().split(' '))
    for j in range(len(sentensce[i])):
        if sentensce[i][j][-1] in string.punctuation:
            punc = sentensce[i][j][-1]
            if sentensce[i][j][0:-1] in wordA:
                sentensce[i][j] = sentensce[i][j][0:-1]
                wrong = wordA.index(sentensce[i][j])
                correct = wordB[wrong]
                sentensce[i][j] = correct + punc
        if sentensce[i][j] in wordA:
            wrong = wordA.index(sentensce[i][j])
            correct = wordB[wrong]
            sentensce[i][j] = correct
for i in sentensce:
    print(*i)
