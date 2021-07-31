# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
# function_name_print("joy","maitri","sohom","rohan","Harry")


def funarg(normal,*args,**kwargs): #The order of the followin arguments are - normal,args,kwargs...
    print(normal)#There are all the specified arguments.
    for item in args:
        print(item)
    print("\nNow i am going to introduce some of our heroes for the presentation.")
    for key,value in kwargs.items():
        print(key,"is our",value)
    # print(args[0])
    # print(type(args)) #it executes as a tuple in the given function.


har = [
    "joy",
    "maitri",
    "sohom",
    "rohan",
    "Harry",
    "The programmer",
    "Maitri.",
    "sobham",
]
normal = "I am a normal argument and the students are ---"
pr = {
    "Joy": "Fitness trainers",
    "Maitri":"Teacher",
    "Harry":"gym trainer.",
    "Shibham":"Cook"
}
funarg(normal,*har,**pr)
