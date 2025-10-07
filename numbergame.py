import random
playing = True
number = str(random.randint(1, 10))
print("i will generate a number between 1 and 10 and you will try to guess  one digit at a time")
print("the game will end when you guess get 1 hero!")
while playing:
    guess = input("enter a number between 1 and 10 and give me best guess \n ")
    if number == guess:
        print("you win")
        print("the number was", number)
        break
    else:
        print("you lose")
        print("try again \n")