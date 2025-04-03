def rabin_karp(t,p):
    d=256
    n = len(t)
    m= len(p)
    h,thash,phash = 1,0,0
    prime = 101
    
    for i in range(m-1):
        h=(h*d)%prime

    for i in range(m):
        thash = (d*thash + ord(t[i]))%prime
        phash = (d*phash + ord(p[i]))%prime

    for i in range(n-m+1):
        if(thash == phash):
            if(t[i:i+m]==p):
                print(f"shift found at index : {i}")
        if(i<n-m):
            thash = (d*(thash-ord(t[i])*h)+ord(t[i+m]))%prime
            if thash < 0:
                thash+=prime

t=input().lower()
p=input().lower()
rabin_karp(t,p)