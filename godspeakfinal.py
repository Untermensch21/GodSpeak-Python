import pyttsx3
from random import randrange
import linecache as lc

engine = pyttsx3.init()
# f=open("godVocab.txt", "r")

engine.say("God says \n")
print("God says")

for i in range(20):
   # mainstring = " "
    rnum = randrange(710)
    print(lc.getline("godVocab.txt", rnum), end="")
    engine.say(lc.getline("godVocab.txt", rnum))
   # thestring = f.readline(rnum)
   # mainstring += (thestring + " " )
    
# print("God says:", mainstring)
    
#engine = pyttsx3.init()
#engine.say("God says")
#engine.say(mainstring)
engine.runAndWait() 




