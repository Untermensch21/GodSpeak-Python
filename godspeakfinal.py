import pyttsx3
from random import randrange
import linecache as lc

engine = pyttsx3.init()


engine.say("God says \n")
print("God says")

for i in range(20):
    rnum = randrange(710)
    print(lc.getline("godVocab.txt", rnum), end="")
    engine.say(lc.getline("godVocab.txt", rnum))

engine.runAndWait() 




