import random
import time

articles = ["a","an", "the"]
prepositions = ["on", "above", "below", "in middle", "in", "out", "center","beside"]
prefixes = ["anti", "auto", "dis", "non","sub"]
sreqWs = ["are","is"]
sreqWs2 = ["am"]

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m","n","p","q","r","s","t","v","w","x","y","z"]

adjectives = ["soft", "hard", "tasty", "sweet", "sour", "spicy", "sticky", "transparent", "opaque", "translucent", "fragile", "loud", "noisy"]
personadjs = ["opaque", "tired", "eating", "working", 'working hard',"sweet"]
nounsPfs = ["I", "you"]
nounsP = ["Ayaan", "Hisham", "someone"]
nounsT =["table", "glass","window", "kitchen", "door", "laptop", "ipad", "oil", "bottle", "fridge", "snake", "paper"]
food = ["cookie", "chicken", "cheese", "fish","burger","tomato"]

writable=["story", "song", 'poem']
drawable = ["picture"]
sitable = ["table", "chair", "sofa"]
breakable = ["glass","window","laptop", "ipad","bottle", "frige"]
smellable = ["book", "flower"]


funnywords = ["koreymonkeeylalala", "TastyMonkeyChicken", "smellytasty Head", "SmellyCooCooBuck"]
actions = ["drawing","sitting", "standing", "running", "writing", "eating", 'breaking', "destroying", "smelling", "firing", "killing"]


sentencestypes = ["describing person", "positioning", "action", "decribing thing"]


#properties of "things"

table = ["hard"] #0
glass = ["fragile"] #1
window = [glass[0]] #2
kitchen = ["Big"] #3
door = ["hard"]#4
laptop = ["expensive"]#5
ipad = ["made by apple"]#6
oil = ["enemy of water"]#7
bottle = ["made of plastic"]#8
fridge = ["cold inside"]#9
snake = ["poisonus and dangerous"]#10
paper = ["flat"]#11




def work():
    ps = random.choice(sentencestypes)

    

    if ps == sentencestypes[0]:
        fSentence = []

        a = random.choice(nounsPfs)
        b = ""
        if a == nounsPfs[0]:
            c = sreqWs2[0]
        elif a == nounsPfs[1]:
            c = sreqWs[0]
        d = ""
        e = random.choice(personadjs)

        fSentence.append(a)
        fSentence.append(b)
        fSentence.append(c)
        fSentence.append(d)
        fSentence.append(e)
        print(fSentence)
    elif ps == sentencestypes[1]:
        fSentence = []

        a = random.choice(nounsPfs)
        b = ""
        if a == nounsPfs[0]:
            c = sreqWs2[0]
        elif a == nounsPfs[1]:
            c = sreqWs[0]
        d = ""
        e = random.choice(prepositions)
        f = ""
        g = "the"
        h = random.choice(nounsT)

        if h == nounsT[0]:
            e = prepositions[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[1]:
            e = prepositions[7]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[2]:
            e = prepositions[7]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[3]:
            e = prepositions[4]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[4]:
            e = prepositions[5]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[5]:
            e = "touching"

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[6]:
            e = prepositions[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[7]:
            e = prepositions[7]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[8]:
            e = "holding"

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[9]:
            e = prepositions[7]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[10]:
            e = prepositions[1]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        elif h == nounsT[11]:
            e = prepositions[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            fSentence.append(e)
            fSentence.append(f)
            fSentence.append(g)
            fSentence.append(h)

        print(fSentence)
    elif ps == sentencestypes[2]:
        fSentence = []

        a = random.choice(nounsPfs)
        b = ""
        if a == nounsPfs[0]:
            c = sreqWs2[0]
        elif a == nounsPfs[1]:
            c = sreqWs[0]
        d = random.choice(actions)

        if d == actions[5]:
            f = random.choice(food)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)
                    fSentence.append(e) 

        
                    fSentence.append(f)
                    print(fSentence)


        if d == actions[4]:
            f = random.choice(writable)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)
                    fSentence.append(e) 

        
                    fSentence.append(f)
                    print(fSentence)

        if d == actions[0]:
            f = random.choice(drawable)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)
                    fSentence.append(e) 

        
                    fSentence.append(f)
                    print(fSentence)


        if d == actions[1]:
            f = random.choice(sitable)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)
                    fSentence.append("on ")
                    fSentence.append(e) 

        
                    fSentence.append(f)
                    print(fSentence)


        if d == actions[2]:
            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            print(fSentence)


        if d == actions[3]:
            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)
            fSentence.append(d)
            print(fSentence)

        if d == actions[6]:
            f = random.choice(breakable)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)
                    fSentence.append(e) 

        
                    fSentence.append(f)
                    print(fSentence)


        if d == actions[8]:
            f = random.choice(smellable)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)
                    fSentence.append(e) 

        
                    fSentence.append(f)
                    print(fSentence)



        if d == actions[10]:
            f = random.choice(nounsP)
            for i in range(len(vowels)):
                if f[0] == vowels[i]:
                    e = "an"

            for ss in range(len(consonants)):
                if f[0] == consonants[ss]:
                    e = "a"
                    fSentence.append(a)
                    fSentence.append(b)
                    fSentence.append(c)
                    fSentence.append(d)

        
                    fSentence.append(f)
                    print(fSentence)


    elif ps == sentencestypes[3]:
        fSentence = []

        a = random.choice(nounsT)
        b = random.choice(sreqWs)
        
        if a == nounsT[0]:
            c = table[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[1]:
            c = glass[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[2]:
            c = window[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[3]:
            c = kitchen[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[4]:
            c = door[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[5]:
            c = laptop[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[6]:
            c = ipad[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[7]:
            c = oil[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[8]:
            c = bottle[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[9]:
            c = fridge[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[10]:
            c = snake[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        elif a == nounsT[11]:
            c = paper[0]

            fSentence.append(a)
            fSentence.append(b)
            fSentence.append(c)

        print(fSentence)




while True:
    work()
    time.sleep(1)