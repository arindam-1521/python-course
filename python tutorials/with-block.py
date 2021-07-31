with open("joy.txt") as f:
    a = f.readlines()  # Here it is not required to close the file .
    print(a)


f = open(
    "joy.txt", "r+"
)  # Here the file will run again because the with open block automatically closes the file after opening ,hence we cans open the file multiple times and read it.
# print(f.readlines())
content = f.readlines()
print(content)
