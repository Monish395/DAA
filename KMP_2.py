def LPS(p):
    m = len(p)
    pi=[]
    pi.append(0)
    k=0
    for i in range(1,m):
        while(k>0 and p[k]!=p[i]):
            k=pi[k-1]
        if p[k]==p[i]:
            k=k+1
        pi.insert(i,k)
    return pi

def KMP(t,p):
    n=len(t)
    m=len(p)
    pi=LPS(p)
    k=0
    for i in range(n):
        while (k>0 and p[k]!=t[i]) :
            k=pi[k-1]
        if p[k]==t[i]:
            k=k+1
        if k==m:
            print(f"shift found at index :{i-m+1}")
            k=pi[k-1]

t="okaplsdnokasdjnqokl"
p="ok"
KMP(t,p)