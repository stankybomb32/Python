s=[1,5,3,6,7,9,2,4,8] #bubble sort
print(s)
s1=s
for pass1 in range(len(s1)-1):
    for i in range(len(s1)-1):
        if s1[i]>s1[i+1]:
            s1[i],s[i+1]=s1[i+1],s[i]
            
print(s1)                               #binary search
key=int(input('Enter key: '))
left=0
right=len(s1)-1
res=-1
while left<=right and res==-1:
    mid=(left+right)//2
    if s1[mid]==key:
        res=mid
    elif s1[mid]>key:
        right=mid-1
    else:
        left=mid+1
print('postion is',res)
