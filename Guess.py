import random
Guess_Word =[
    "trail","worse","block","taken","beach","wrong","cloud"
]
randomNum = random.randint(0,len(Guess_Word)-1)
chosen_word = Guess_Word[randomNum]
##Game Init State
Displayed_Text = ["-","-","-","-","-"]
Life_Remain = 5
GameState = "PLAYING"

##Game Function
def check_Guess(Guess):
    global Life_Remain
    index = chosen_word.find(guess)
    if index in range(5):
        Displayed_Text[index] = guess
        print(Displayed_Text)
        return Life_Remain

    else:
        Life_Remain = Life_Remain-1
        print("wrong guess")
        return Life_Remain
def isGuessed():
    if "-" in Displayed_Text:
        return False
    else:
        return True
def check_Life():
    global Life_Remain
    global GameState
    if Life_Remain <= 0:
        GameState = "LOSE"
    return GameState
    
##IO 
print(chosen_word)
while isGuessed() == False:
    if GameState == "PLAYING":
        guess = input("Guess : ")
        if len(guess) != 1:
            print("Input must a character")
        elif guess.isdigit():
            print("Input must a alphabet")
        else:
            Life_Remain = check_Guess(guess)
            GameState = check_Life()
    elif GameState == "LOSE":
        print("Lose")
        break

if isGuessed() == True:
    print("Word Guessed")
