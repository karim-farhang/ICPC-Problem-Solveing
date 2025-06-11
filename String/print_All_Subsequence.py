arr = list()
def allseq(s,out):
    if len(s) == 0:
        arr.append(out)
        return
    allseq(s[1:],out+s[0])
    allseq(s[1:],out)
s = input()
start,end = map(int,input().split(' '))
start-=1
end-=1
s = s[start:end]
out = ""
allseq(s,out)
print(arr)