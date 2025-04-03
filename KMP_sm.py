def prefix_finder(p):
    m = len(p)
    pi=[]
    pi.append(0)
    k=0
    for q in range(1,m):
        while k>0 and p[k] != p[q]:
            k = pi[k-1]
        if p[k] == p[q]:
            k=k+1
        pi.insert(q,k)
    return pi

def KMP(t,p):
    n = len(t)
    m = len(p)
    pi = prefix_finder(p)
    k=0
    for i in range(n):
        while k>0 and p[k]!=t[i]:
            k=pi[k-1]
        if p[k] == t[i]:
            k=k+1
        if k==m:
            print(f"shift occurs at index : {i-m}")
            k=pi[k-1]

t = input("Enter text : ")
p = input("Enter pattern : ")
KMP(t,p)