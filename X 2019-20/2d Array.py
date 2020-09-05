a1=[
    [2,9,3,-4],
    [7,11,-1,0],
    [2,8,9,18]
    ] #3x4 array rc model
##print(a1[0][2])
marks=[
    ['Priyo','Sadik','Adib','Sami'],
    [100,99,69,0],
    [80,81,42,0]
    ]
avgCS=0 #T1
totalCS=0
for i in marks[1]:
    totalCS+=i
avgCS=totalCS/(len(marks[1]))
print(avgCS)

studentAvg=0 #T2
counter=0
for i in marks[0]:
    studentAvg=(marks[1][counter]+marks[2][counter])/2
    print(i+'\'s marks avg is',studentAvg)
    counter+=1
