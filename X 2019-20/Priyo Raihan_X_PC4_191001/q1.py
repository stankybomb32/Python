global numChild
global numMid
global numSenior

numChild=3        #preadded values
numMid=3
numSenior=2
numTotal=numChild+numMid+numSenior
costChild=20
costMid=30
costSenior=25
costTotal=(numChild*costChild)+(numMid*costMid)+(numSenior*costSenior)
print('The total cost is',costTotal)

def addVisitor(age): #function needs to be called
    if age<16:
        numChild=numChild+1
    elif age<60:
        numMid=numMid+1
    else:
        numSenior=numSenior+1
    print('Visitor Added')
    print('Children=',numChild)
    print('Mid=',numMid)
    print('Senior=',numSenior)
    print('Total=',numTotal)
    print('\nHence the total cost is',costTotal)
