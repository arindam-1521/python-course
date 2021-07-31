# def print2(str1):
#     print2(str1) #This function never breaks so it throws the error as recursion error.
#     print("This is ",str1)
# print2("joy  and he is a good boy and he is very gentle to the all of his parents.")
# def factorial(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#     return fac
#     """
#     param n : Integer number
#     return : n * (n - 1) * (n - 2) ......3 * 2 * 1
#     """
#     pass


# number = int( #This is an iterative function.
#     input("Enter your number here for knowing the factorial value of the number: ")
# )
# print(factorial(number))


def factorial_recursive(n):
    """
    parameter n : Integer number
    return : n * (n - 1) * (n - 2) ......3 * 2 * 1
    """
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = int(  # This is an recursive function.
    input("Enter your number here for knowing the factorial value of the number: ")
)
print("The factorial of the following number is ", factorial_recursive(number))
print(factorial_recursive.__doc__)
print("Hello world")
