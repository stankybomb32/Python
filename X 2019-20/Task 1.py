def numSum(begin,end):
    s=0
    for i in range(begin,end+1):
       s+=i
    print('The sum of numbers between',begin,'and',end,'is',s)

def numProduct(begin,end):
    p=1
    for i in range(begin,end+1):
        p=p*i
    print('The product of numbers between',begin,'and',end,'is',p)
    
          
