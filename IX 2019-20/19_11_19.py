

def sigma(p,q):
    s=0
    for p in range(p,q+1,1):
        s+=4*p**3
    return(s)

print(sigma(41,50)+ sigma(51,60)==sigma(41,60))
##print()

def fib(n):
    a=b=1

    for p in range(1,n+1):
        print (b)
        a,b=b,a+b
        
fib(500000000000000000000000)
 
