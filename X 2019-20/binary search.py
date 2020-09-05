def binarySearch(array,key):
    left=0
    right=len(array)-1
    res=-1
    while left<=right and res==-1:
        mid=(left+right)//2
        if array[mid]==key:
            res=mid
        else:
            if array[mid]>key:
                right=mid-1
            else:
                left=mid+1
    return res
