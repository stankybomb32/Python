marks=[20,25,10,5,29]
print(marks)
def markSum(li):
    mSum=0
    for i in li:
        mSum=mSum+i
    print('Sum of Marks is',mSum)
markSum(marks)
def marksAvg(li):
    mAvg=0
    for i in li:
        mAvg=mAvg+i
        mAvg=(mAvg/len(li))
    print('Average of the Marks is',mAvg)
marksAvg(marks)
