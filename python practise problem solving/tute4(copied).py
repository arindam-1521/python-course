n = 12
guess = 1
print("Number of guesses is limited to 9")
while guess <= 9:
    guess_number = int(input("Enter your number to start the game:"))
    if guess_number < n:
        print("You have written a smaller number try something bigger.")
    elif guess_number > n:
        print("You have written a larger number try something")
    else:
        print("You have won the game.yay!!!!!!!")
        print(guess, "no of guesses you took to finish the game")
        break
    print(9 - guess, "no of guesses you have")
    guess = guess + 1
if guess > 9:
    print("You lost the game")
    print("Try again for the next time to win the game.")
