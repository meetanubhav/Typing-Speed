from time import time
import random

def TestSentence():
    s1= "This is america. And we have Donal Trump as our president. Califonia is known as silicon valley. "
    s2="Big fox ate a little dog."
    corpus=list()
    corpus=[s1,s2]
    return(random.choice(corpus))

def getString():
    getText=TestSentence()
    CharString=list()
    # putting string into list
    for getText in getText:
        CharString.append(getText)

    # System String lenght 
    StringLen=len(CharString)
    getUserString(CharString,StringLen)

    # print(CharString,StringLen)

def getUserString(CharString,StringLen):
    print('Begin :')
    for i in range (0,StringLen):
        getuserInput=input()
        if(getuserInput==CharString[i]):
            print('success')
        else:
            break

if __name__ == "__main__":
    # Clear screen(cmd/terminal)
    # _ = call('clear' if os.name =='posix' else 'cls')
    getString()