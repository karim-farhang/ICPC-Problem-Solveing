n = int(input())
gene = list(map(str,input().split(' ')))
gene_val = list(map(str,input().split(' ')))
q = int(input())
while q > 0:
    s,f,d = map(str,input().split(' '))
    s = int(s)
    f = int(f)
    print(gene[s:f])
    q-=1