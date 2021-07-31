#This is a prgramm which continues to take input from the user and stops the process when the input is greater than 100
while(True):
    inp = float(input("Enter a number:\n"))
    if inp >100.0:
        print("congrats")
        break
    else:
        print("Try again.")
        inp = inp +1
        print(inp)
        
        continue
