import random

words = ['chicken','fish','dog','god','of','nice','ok','what','look','rat','bat','fat']
eng_ltrs = 'a b c d e f g h i j k l m n o p q r s t u v w x t z'
eng_ltrs = eng_ltrs.split(' ')
print(eng_ltrs)
man = 5
chops = 0
in_game = False
def main():
    global chops
    global man
    global in_game
    word = random.choice(words)
    count = len(word)
    guesses = []
    ltrs = []
    for i in word:
        ltrs.append(i)
    in_game= True
    while in_game:
        print('Numebr of letters : '+str(count))
        if man <= 0:
            print('Game Over')
            in_game= False
        else:
            letter = input('Enter Letter: ')
            if letter in ltrs:
                
                if len(guesses) == count:
                    print('Game Won!')
                    in_game=False
                else:
                        if letter in guesses:
                            print('letter is already completed')
                            
                        else:
                            guesses.append(letter)
                            count=count-1
                            if len(guesses)== count:
                                print('Game Won!')
                                in_game = False
            
                        
            else:
                chops +=1
                man =man-1
                print('Chances: '+str(man))
            

main()

    
    