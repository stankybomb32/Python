marks=[20,25,10,5,29]
print(marks)
def markSum(li):
    mSum=0
    for i in li:
        mSum=mSum+i
    print('Sum of Marks is',mSum)
markSum(marks)
