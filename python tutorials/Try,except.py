

num1 = (input("Enter the number 1:"))
num2 = (input("Enter the number 2:"))
try: #at first it tries to check if the process is possible or not,if yes then it runs and if not then it goes to the except statement.
    print("The sum of the two numbers is ",
        int(num1)+int(num2))
except Exception as e: #This is a way to print the error as the string statement.
    print(e)
    
    
print("This number is very important.")