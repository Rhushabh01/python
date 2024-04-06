import random

target = random.randint(1, 1000)

while True:
    user_value = int(input("Guess a random number between 1 to 1000 or you can quit the game "))
    if(user_value == "quit"):
        break
    
    user_value = int(user_value)
    if(user_value == target):
        print("congratulations you won the game!")
        break
        
    elif(user_value < target):
        print("your guess is smaller than the target value!")
        
    else:
        print("your guess is greater than the target value!")
        
print("GAME OVER")
