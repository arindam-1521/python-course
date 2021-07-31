# def function1():
#     print("subscribe now.")
# func2 = function1
# del function1
# func2()#Here the function 2  is executed because the function already is been copied.

# def funcret(number):
#     if number == 0:
#         return print
#     if number == 1:
#         return sum
# print(funcret(1))

# def executer(function1):
#     function1("This")
# executer(print)

def dec1(function1):
    def nowexec():
        print("Executing now")
        function1()
        print("Executed")
    return nowexec
# @decl1
def whoisharry():
    print("Harry is a good boy")
whoisharry = dec1(whoisharry)

whoisharry()