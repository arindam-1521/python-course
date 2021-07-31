# l = 4 #This is a global variable.Which is does not affected by the functional value inside the function.

# def function1(n):
#     l = "He is a programmer."
#     m = "He is a great person."
#     print(l,m)
#     print(n,"I have print it using the function")
#     return("Thanks for using.")
# print(function1("This is me joy here."))

x = 67
def joy():
    x = 56
    def rohan():
        global x #This executes the function outside the function because it absolutely go outside the function.
        x = 88 #This global variable always executes the value and it overwrites the value outside the function itself..
    print("Before calling rohan " ,x)
    rohan()
    print("After calling rohan " ,x)
joy()
print(x)  