# # a = 9
# # b = 5



# c = sum((a,b)) #this is a buils function in python.
# print(c)
# def function(a,b,c):
#     print("Hello you are function didi.",a+b+c)
# function(2,3,4)


def function(a,b): #Here this defines a function
    '''This is a function which return the average value of the two numbers.'''
    average = (a+b)/2
    # print("The average of the two numbers",average)
    return("The return value of the function is ",average) #The value that a function returns as output for the every input going into the function.
# v = function(3,5)
# print(v)
print(function.__doc__) #Here __doc__ defines the dockstring which giver us the information about the function.
