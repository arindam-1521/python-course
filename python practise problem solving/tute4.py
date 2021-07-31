n = 23
guess = 1
while (guess<9):
    inp = int(input("Enter your number Here:"))
    if inp < n:
        print(f"Your number is lesser than the magic number")
        print("Try agian")
    if inp > n :
        print(f"Your number is greater than the magic number")
        print("Try agian")
    if inp == n:
        print("Congrats you hit the magic number")
        break
