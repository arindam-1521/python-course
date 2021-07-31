# My first game in python using very simple and straight logic.
import pyttsx3
friend = pyttsx3.init()
friend.say("Let's start the game.....It is going to be a fun activity for all of us.")
friend.runAndWait()
import random
from playsound import playsound

my_point = 0
computer_point = 0
print("Let's Start The Rock Paper Scissors Game\n")
playsound("intro.wav")
while True:
    list = ["stone", "paper", "scissors"]
    computer_choice = random.choice(list)
    a = 5
    if computer_point == a:
        print("You lose!!!!!!!!!!!!")
        playsound("fail-buzzer-03.mp3")
        friend.say("alas you lost the game.....")
        friend.say("Thanks for Playing the game")
        friend.runAndWait()
        break
    elif my_point == a:
        print("You win!!!")
        playsound("anime-wow-sound.mp3")
        friend.say("Congrats you won the game...yay!!!")
        friend.say("Thanks for playing the game..")
        friend.runAndWait()
        break
    if computer_choice == "stone":
        my_choice = input(f"Enter a word from {list}")
        if my_choice == "stone":
            playsound("wet.wav")
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
        elif my_choice == "scissors":
            playsound("rock.wav")
            playsound("lose.wav")
            computer_point = computer_point + 1
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
        elif my_choice == "paper":
            playsound("paper.wav")
            playsound("win.wav")
            my_point = my_point + 1
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
    elif computer_choice == "scissors":
        my_choice = input(f"Enter a word from {list}")
        if my_choice == "scissors":
            playsound("wet.wav")
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
        elif my_choice == "paper":
            playsound("scissors.mp3")
            playsound("lose.wav")
            computer_point = computer_point + 1
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
        elif my_choice == "stone":
            playsound("rock.wav")
            playsound("win.wav")
            my_point = my_point + 1
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
    elif computer_choice == "paper":
        my_choice = input(f"Enter a word from {list}")
        if my_choice == "paper":
            playsound("wet.wav")
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
        elif my_choice == "stone":
            playsound("paper.wav")
            playsound("lose.wav")
            computer_point = computer_point + 1
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
        elif my_choice == "scissors":
            playsound("scissors.mp3")
            playsound("win.wav")
            my_point = my_point + 1
            print(f"Your score is {my_point}")
            print(f"computer score is {computer_point}")
            print("Computer chosed ", computer_choice)
            continue
