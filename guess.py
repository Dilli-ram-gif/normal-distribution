import random

random_number = random.randint(1,101)
print(random_number)
#Guessing the number

total = 0
def guessing_number():
    
    guess_number = int(input("Enter the guessing number: "))

    if random_number == guess_number:
        print("You won!")
        print("Your total attempts are: ",total)
    elif random_number < guess_number:
        print("Guess the lower")
        guessing_number()
    elif random_number > guess_number:
        print("Guess the upper")
        guessing_number()
    else:
        exit()
        
guessing_number()