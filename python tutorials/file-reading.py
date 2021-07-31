# File io basics
f = open("demo.txt", "r+")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read(344)
# for line in f:
#     print(line,end="")
# print(content)
print(f.readlines())
# content = f.read(344)
# print("2",content)
f.close()


# f = open("joy.txt","r+")
# content = f.read()
# print(content)
# f.write("\nHello user thank you for using the method to edit the page.")
