num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = input("choose the operator from + - * / :")
if operator == "+":
    if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45 :
        print("The answer of the following problem is " +str(555))
    else:
        print("The answer of the following problem is " +str(num1+num2))
if operator == "-":
    if num1 == 56 and num2 == 1 or num1 == 1 and num2 == 56  :
        print("The answer of the following problem is " +str(145))
    else:
        print("The answer of the following problem is " +str(num1-num2))
if operator == "*":
    if num1 == 120 and num2 == 3 or num1 == 3 and num2 == 120 :
        print("The answer of the following problem is " +str(568))
    else:
        print("The answer of the following problem is " +str(num1*num2))
if operator == "/":
    if num1 == 15 and num2 == 3 or num1 == 3 and num2 == 15 :
        print("The answer of the following problem is " +str(45))
    else:
        print("The answer of the following problem is " +str(num1/num2))
