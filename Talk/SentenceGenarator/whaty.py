import random




def find():
    wordt = input("mention a word as the subject of the sentence I am going to make (can only take 1 word: to use multiple words use capital letter of the words after the first word. Dont use spaces in between. eg: friedEggs ): ")

    tomato = ["tomatos are tasty", "tomatos are red"]
    chicken = ["My favourite animal","chickens eat grains"]
    friedEggs = ["sometimes smelly", "I ate it for breakfast"]
    ball = ["fun to play with", "balls are round"]
    laptop = ["is expensive", "made by different companies"]
    mobile = ["poket-portable","only people above age 18 can use it"]
    pillow = ["pillows are soft","on what I keep my head on when I sleep"]
    

    words = {"tomato":tomato,
             "chicken":chicken,
             "friedEggs": friedEggs,
             "ball": ball,
             "laptop" : laptop,
             "mobile": mobile,
             "pillow": pillow
             }


    if words.__contains__(wordt):
        print(random.choice(words.__getitem__(wordt)))
        print("\n")

    elif wordt == "stop()":
        exit()
    else:
        print("Object not found \n")


while True:
    find()