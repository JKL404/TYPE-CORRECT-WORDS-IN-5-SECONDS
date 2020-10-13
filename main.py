import random
import time
from spellchecker import SpellChecker
user1=[]
user2=[]
spell = SpellChecker()

letter1=''
letter2=''
print("Welcome to __TYPE CORRECT WORDS IN 5 SECONDS__ Game:")
print("________________________________________________")
print("Rules:\n1.Time Limit 5 Seconds\n2. Correct words\n")
option=input("Do you wanna Start? yes/no")
if(option=="yes"):
    print("Its Jack turn:")
    ready=input("Are you ready Jack? yes/no\n=>\t ")
    if(ready=="yes"):
        letter1=random.choice('abcdefghijklmnopqrstuvwxyz')
        prompt = "You have 5 seconds to choose the correct answer...\n" 
        print(prompt + "\n Your Letter is ",letter1)
        t_end = time.time() + 5
        while time.time() < t_end:
            user1.append(input("Input words:"))
    print("Time UP\n\nIts Jill turn:")
    ready=input("Are you ready Jill? yes/no\n=>\t ")
    if(ready=="yes"):
        letter2=random.choice('abcdefghijklmnopqrstuvwxyz')
        prompt = "You have 5 seconds to choose the correct answer...\n"
        print(prompt + "\n Your Letter is ",letter2)
        t_end = time.time() + 5
        while time.time() < t_end:
            user2.append(input("Input words:"))
        print("Time UP\n\n")    
class Alexa():
    def __init__(self, word,letter):
        self.word = word
        self.letter=letter
        self.score=[]
    def check_spelling(self):
        count=0
        for w in self.word:
            if w[0].lower() == self.letter:
                if w==spell.correction(w):
                    count+=1
                    self.score.append(w)
        return(count)         
a1=Alexa(user1,letter1)
u1=a1.check_spelling()

a2=Alexa(user2,letter2)
u2=a2.check_spelling()
print("==================================")
print("Jack Correct Words:\n",a1.score)
print("Jil Correct Words:\n",a2.score)
print("==================================")
if(u1 > u2):
    print("The winner is Jack")
else:
    print("The winner is Jil")
print("==================================")
