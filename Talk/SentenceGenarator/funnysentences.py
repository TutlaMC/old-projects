import time
import random

nouns = ['snake','cat','dog','bug','chicken','laptop','leaf','fire','bottle','water','book',"mouse","feet","canvas","table","toilet","me","a cliff","pants","aairah's pants","dedamama","dinchu's moustache","mama","a fart","bahamas","morroco","dinchu's belly","dedama's big big fart"]
verb = ['eat','drink','sleeps on','cook','smell',"pokemoned","exploded","farted","farted in","exploded a mexican in the toilet","pooped","jumped off", "poisoned","killed","fought","beat","wresteled","punched a","peed","wore"]

while True:
    print(random.choice(nouns)+' '+random.choice(verb)+' '+random.choice(nouns))
    time.sleep(0.8)



