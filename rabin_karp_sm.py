def rabin_karp(t,p):
    d=256 #for alpha strings
    prime = 101
    n,m = len(t),len(p)
    thash,phash,h = 0,0,1
    s=[]

    for i in range(m-1):
        h = (h*d)%prime

    for i in range(m):
        thash = (d*thash + ord(t[i]))%prime
        phash = (d*phash + ord(p[i]))%prime

    for i in range(n-m+1):
        if(thash == phash):
            if t[i:m+i] == p:
                s.append(i)

        if i<n-m:
            thash = (d*(thash-ord(t[i])*h)+ord(t[i+m]))%prime
            if thash < 0:
                thash+=prime
    return s

t = input("Enter text : ")
p = input("Enter pattern : ")
s = rabin_karp(t,p)
print(s)