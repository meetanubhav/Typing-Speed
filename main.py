import time
import random
import msvcrt
Start_time=0
def TestSentence():
    s1= "This is america. "
    s2="Big fox ate a little dog."
    s3='And we have Donal Trump as our president.'
    s4='Califonia is known as silicon valley.'
    corpus=list()
    corpus=[s1,s2,s4,s3]
    return(random.choice(corpus))

def getString():
    getText=TestSentence()
    CharString=list()
    print(getText)
    # putting string into list
    for getText in getText:
        CharString.append(getText)

    # System String lenght 
    StringLen=len(CharString)
    getUserString(CharString,StringLen)

def getUserString(CharString,StringLen):
    print('Begin :')
    error=0
    correct=0
    global Start_time
    Start_time=time.time()
    # print(CharString)
    for i in range (0,StringLen):
        # getuserInput=raw_input()
        # print(CharString[i])
        getuserInput = msvcrt.getch()
        print(getuserInput)
        check=calculate(CharString,getuserInput,i)
        if(check==1):
            correct=correct+1
        else:
            error=error+1
    result(correct,error)

def calculate(CharString,getuserInput,i):
    if(ord(getuserInput)==ord(CharString[i])):
    	return(1)
    else:
        return(0)

def result(correctCount,errorCount):
    print('Correct Count : \t',correctCount)
    print('\nError Count : \t',errorCount)
    tm=(time.time()-Start_time)/10
    print('Time taken =',"%.3f" %tm,' ms')
if __name__ == "__main__":
    # Clear screen(cmd/terminal)
    # _ = call('clear' if os.name =='posix' else 'cls')
    getString()
