import random

say = print

command = None
commands={'get jails':'people jail numbers', 'people in jails':'Says the in/out of people in jail','add person':'adds person'}
theifs = {
    'simion':12,
    'Fodeo Popa':17,
    'Yanker frogila':2,
    'fraub fraud':43,
    'Dinky stoneWall':54,
    'fooper gabela':3,
    'Frus Eper':15,
    'Buckuty cup':30,
    'Yander Sim':345,
    'Twatty Lin':567,
    'Pampy Lin':87
    }
theifsInOut = {
    'simion':'in',
    'Fodeo Popa':'in',
    'Yanker frogila':'in',
    'fraub fraud':'in',
    'Dinky stoneWall':'in',
    'fooper gabela':'in',
    'Frus Eper':'in',
    'Buckuty cup':'in',
    'Yander Sim':'in',
    'Twatty Lin':'in',
    'Pampy Lin':'in'
    }


while command != '::exit::':
    command = input('>>> ')
    if 'get jails' in command:
        say(theifs)
    elif command == 'people in jails':
        say(theifsInOut)
    elif command == 'add person':
        person_N = input('Name: ')
        person_JN = None
        def nj():
            global person_JN
            global person_N
            global theifs
            global theifsInOut
            person_JN = input('Jail number')
            if person_JN in theifs.keys():
                say('Jail number: '+person_JN+" is aldready used")
                nj()
            theifs[person_N] = person_JN
            theifsInOut[person_N] = 'in'
        nj()
    elif 'punishment' in command:
        punishments = ['Shoot the butt','Perma-Sticker the butt','Hit your head to the wall 2 times']
        say(random.choice(punishments))
    else:
        say('in <stdin> ln <current>')
        say(command+' is not refered in list:commands \n Maybe <user> meant <command> is \n')
        say(str(commands)+'\n',end='\n')
