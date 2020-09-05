r=0
while r<1:
    name=str(input('Hello there! Tellme your name, please\n:'))
    mEnglish=float(input('Enter your mark in English, '+name+'\n:'))
    mBangla=float(input('Enter your mark in Bangla, '+name+'\n:'))
    mCS=float(input('Enter your mark in Computer Science, '+name+'\n:'))
    sMarks=[name,[mEnglish,mBangla,mCS]]
    print('Inputted Data: ',sMarks)
    total=(mEnglish+mBangla+mCS)
    avg=total/(len(sMarks[1]))
    print(name+', your total is ',str(total),' and average is '+str(avg))
    inp=input('Press X to terminate or anything else to redo.\n:')
    if inp=='X' or inp=='x':
        r=1
