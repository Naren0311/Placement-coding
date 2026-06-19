def fibbo(n):
    m=(n+1)//2
    a=1
    b=1
    c=[]
    for _ in range(m):
        c.append(a)
        a,b=b,a+b
    return c
def primes(n):
    m=n//2
    num=2
    count=0
    d=[]
    while count<m:
        is_prime=True
        i=2
        while i*i<=num:
            if num%i==0:
                is_prime=False
                break
            i+=1
        if is_prime:
            d.append(num)
            count+=1
        num+=1
    return d
n=11
c=fibbo(n)
d=primes(n)
j=0
k=0
for i in range(1,n+1):
    if i%2==0:
        print(d[j],end=" ")
        j+=1
    else:
        print(c[k],end=" ")
        k+=1

        
        
