marks=[
    ['Asif',81,78,55],
    ['Babur',87,71,62],
    ['Hasib',90,81,66],
    ['Zahir',78,74,62]
    ]
#1. Display total mark, average mark along side the student.
#2. Display the performance of Class X in E,B and CS
#3. Rearrange the students in descending order of the marks in cs.

def total(li):
    n=0
    while n<len(li):
        i=1
        s=0
        while i<(len(li[n])):
            s=s+(li[n][i])
            i=i+1
        avg=s/(len(li[n])-1)
        print(li[n][0],'got',s,'in total and his average is',avg)
        n=n+1
             
def subject(li):
    for i in li:
        print(i[0],'got',i[1],'in English',i[2],'in Bangla and',i[3],'in CS')

bMarks=marks
rMarks=[]
repeat=True
while repeat==True:
    i=0
    while i<(len(marks)-1):
        if bMarks[i][3]>bMarks[i+1][3]:
            bMarks[i]=bMarks[i]
        else:
            bMarks.append(marks[i+1])
    i=0
    while i<len(bMarks):
        if bMarks[i][3]>bMarks[i+1]:
            repeat=False
        else:
            repeat=True
