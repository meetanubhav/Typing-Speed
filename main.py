# from time import time
import random
from os import system, name

def TestSentence():
    s1= "This is america. And we have Donal Trump as our president. Califonia is known as silicon valley. "
    s2="Big fox ate a little dog."
    corpus=list()
    corpus=[s1,s2]
    return(random.choice(corpus))

def getString():
    getCharacter=input('Enter string the above string : \n')

if __name__ == "__main__":
    _ = call('clear' if os.name =='posix' else 'cls')
    getText=TestSentence()
    print(getText)
    getString()