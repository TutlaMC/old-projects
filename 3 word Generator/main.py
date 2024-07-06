from random import *
from time import *
from tkinter import *
words = ['and','bye','age','app','not','use','try','why','ill','top','one','day','you','tip','pie','two','hat','mat','log','leg','tap','fog','ant','his','hey','hot','old','cot']

with open('twords.txt','r') as file:
   
    # reading each line    
    for line in file:
   
        # reading each word        
        for aword in line.split():
   
            # displaying the words           
            words.append(aword)

nwrds = 0
nnwrds = ''
gword = []
tries = 0
t_tries = 0
words_made = 0
letters = 'abcdefghijklmnopqrstuvwxyz'
word = ''
def run():
    word = ''
    for i in range(3):
        word += choice(letters)
    if word in words:
        return [True,word]
    else:
        return [False,word]
    print(word)

loop = 10000


for i in range(loop):
    tries = 0
    while word not in words:
        a = run()
        if a[0] == True:
            tries+=1
            t_tries+=1
            words_made+=1
            cat = ''+'word: '+a[1]+' tried: '+str(tries)+' times'
            gword.append(cat)
            nnwrds+='\n'+a[1]
            #print('\n','word: ',a[1])
            #print('tried: ',tries,'times')
            break
            break
        else:
            tries+=1
            t_tries+=1
            nwrds += 1
            nnwrds+='\n'+a[1]
    #print('In ',t_tries,' tries made ',words_made,' words')
    

    
print('words:')
wrds =''
for i in range(len(gword)):
    wrds+=gword[i]
    wrds+='\n'

with open('Words.txt','x') as file:
    sntnc = 'number of Words made: '+str(nwrds)+'\n+Proper Words made: '+str(words_made)+'\n Total tries: '+str(t_tries)+'\n'+'\n\n\n'+str(wrds)+'\n'+'\n\n All words:\n\n'+nnwrds
    file.write(sntnc)

print(wrds)
    

