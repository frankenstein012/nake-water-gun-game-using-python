import random
def gameWinner(computer, you):

    if computer == you:
        return None

    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn -> ")
randNum = random.randint(1, 3)
if randNum == 1:
    computer = 's'
elif randNum == 2:
    computer = 'w'
elif randNum == 3:
    computer = 'g'

you = input("Your Turn -> Snake(s) or Water(w) or Gun(g) ")

a = gameWinner(computer, you)

print(f"Computer choose {computer}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!  :( ")
elif a:
    print("You Win the game!")
else:
    print("You Lose , try again once !")
