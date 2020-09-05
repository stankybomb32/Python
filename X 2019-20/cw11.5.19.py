##for n in range(-10,11):
##    s=str(n**3-5*n**2).zfill(8)
##    print(s)
##for n in range(-10,11):
##    print(str(n**3-5*n**2).rjust(8))
##

marks=[
    ['Arif',85],
    ['Babul',73.5],
    ['Hamid',80],
    ['Adnan',81.5]
    ]
total=0
print(('Students'.ljust(8))+('Marks'.rjust(8)))
print('--------------------')
for i in marks:
    s=i[0].ljust(8)+str(float(i[1])).rjust(8)
    print(s)
    total=total+i[1]
print('--------------------')
print(('Total'.ljust(8))+str(total).rjust(8))
