loginName = 'Apollo'#assumed name and pwd
pwd= '123'
maxTrial=3

while maxTrial>0:
    curName=input('Please enter your login name: ')
    curPwd=input('Please enter password: ')
    print()# this print statement puts a blank line
    
    if curName == loginName and curPwd == pwd:
        print('Now login program will take you to the main program.')
        break# statement puts the execution pointer immediately after "while" block
    else:
        print('Invalid credential provided.')
        # maxTrial=maxTrial - 1
        maxTrial-=1

        if maxTrial>0:
            print ("You have",maxTrial,'more trials.')

        print()# this print statement puts a blank line
        if maxTrial==0:
            print('Access Denied.')
