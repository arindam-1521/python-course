#``````````````````````````````Map`````````````````````````````
# numbers = ["2","3","4","5","6","7","8","9"]
# numbers = list(map(int,numbers)) #This is a map function which interconverts the elements of the language.
# # for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# numbers[3] = numbers[4] + 1
# # print(numbers)

# num = [2,3,4,5,6,7,8,9]
# def sq(a):
#     print(a**2)
# square = [list(map(sq,num))]

# num = [2,3,4,5,6,7,8,9]
# square = [list(map(lambda x:x**2,num))] #The map function executes the following function in the later and every element of the list.
# print(square)


# def square(a):
#     return a**2
# def cube(a):
#     return a**3
# func = [square,cube]
# for i in range(4):
#     vao = list(map(lambda x:x(i),func))#Here x is function that returns a value if a function is given to it.
#     print(vao)

# ````````````````````````Filter`````````````````````````#
list1 = [1, 2, 3, 4, 5, 6, 7]


# def is_greater(num):
#     return (
#         num > 5
#     )  # This function returns true is the followiung data is correct for the given ouptut otherwise it gives False as the output.


# gr_than = list(
#     filter(is_greater, list1)
# )  # Filter function returns the following value when the statement in it is true.
# print(gr_than)

# ````````````````````````````Reduce``````````````````````#]
from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7] #Here the reduce function executes the first function to the later value of the code.in the following example lambda function is executed to the list1;

num = reduce(lambda x,y:x+y,list1)
# i = 0
# num = 0
# for i in list1:
#     num = num + i
# print(num)
print(num)