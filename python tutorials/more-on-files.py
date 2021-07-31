# f = open("joy.txt")
# # print(f.tell())
# print(f.readline())
# print(f.tell())
# # print(f.tell())
# # print(f.readline())
# # print(f.tell())
# f.seek(3)
# print(f.readline())
# # print(f.tell())
f = open("joy.txt", "r+")
print(f.tell())
print(
    f.readline()
)  # The readline function reads one line of the following text and then prints it in to the output center.
print(
    f.tell()
)  # The tell function tells us that how many characters are print during the line which is very helpful for the indexing of the characters.
print(f.readline())
print(
    f.tell()
)  # The seek function moves back the pointer to the requred position for the ease of learning.
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(43)
print(f.readline())
f.seek(0)
print(f.readline())
f.close()  # Note- It is must to close the file after opening it because it is a very good practise for the begginers.
# after the seek function the new line is read from the following index given inside the seek function.
