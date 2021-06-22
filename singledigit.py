t=int(input())
for i in range(t):
     m,n,x=map(int,input().split())
     su(m,n,x)

def su(m,n,x):
    s=0
    c=0
    while m<=n:
        while m!=0:
            s=s+m%10
            m=m//10
        if s==x:
            c=c+1
        else:
            return su(s)
    print(c)
    m=m+1

