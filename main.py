import random

# Take the random integer
randomno = random.randint(1,50)
print(randomno)
guesses = 0
userguess = None

while(userguess != randomno):
    userguess = int(input("Enter your guess: "))
    guesses += 1

    if userguess == randomno:
        print("***************************************************")
        print("You have guessed correct")
        print("You gussed the correct answer in:", guesses, "Attempt")
        print("***************************************************")

    else:
        if userguess > randomno:
            print("Please Enter Lower Number ")
        else:
            print("Please Enter Higher Number ")



# Count Gusses

    