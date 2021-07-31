# Health management system
def gotdate():
    import datetime

    return datetime.datetime.now()


print(gotdate())


def take(k):
    if k == 1:
        c = int(input("Enter 1 for excercise and 2 for food:"))
        if c == 1:
            value = input("Type Here:\n")
            with open("Joy-ex.txt", "a") as op:
                op.write(str([str(gotdate())]) + ":" + value + "\n")
                print("successfully written.")
        elif c == 2:
            value = input("Type Here:\n")
            with open("Joy-food.txt", "a") as op:
                op.write(str([str(gotdate())]) + ":" + value + "\n")
                print("successfully written.")
    elif k == 2:
        c = int(input("Enter 1 for excercise and 2 for food:"))
        if c == 1:
            value = input("Type Here:\n")
            with open("Rohan-ex.txt", "a") as op:
                op.write(str([str(gotdate())]) + ":" + value + "\n")
                print("successfully written.")
        elif c == 2:
            value = input("Type Here:\n")
            with open("Rohan-food.txt", "a") as op:
                op.write(str([str(gotdate())]) + ":" + value + "\n")
                print("successfully written.")
    elif k == 3:
        c = int(input("Enter 1 for excercise and 2 for food:"))
        if c == 1:
            value = input("Type Here:\n")
            with open("Maitri-ex.txt", "a") as op:
                op.write(str([str(gotdate())]) + ":" + value + "\n")
                print("successfully written.")
        elif c == 2:
            value = input("Type Here:\n")
            with open("Maitre-food.txt", "a") as op:
                op.write(str([str(gotdate())]) + ":" + value + "\n")
                print("successfully written.")


def retrive(k):
    if k == 1:
        c = int(input("Enter 1 for excercise and 2 for food:"))
        if c == 1:
            with open("Joy-ex.txt") as op:
                for i in op:
                    print(i, end="")
        if c == 2:
            with open("Joy-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for excercise and 2 for food:"))
        if c == 1:
            with open("Rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        if c == 2:
            with open("Rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for excercise and 2 for food:"))
        if c == 1:
            with open("Maitri-ex.txt") as op:
                for i in op:
                    print(i, end="")
        if c == 2:
            with open("Maitri-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter a valid input:")


print("Halth management system: ")
a = int(input("press 1 for look and 2 for retrieve: "))

if a == 1:
    b = int(input("press 1 for joy 2 for rohan and 3 for maitri: "))
    take(b)
else:
    b = int(input("press 1 for joy 2 for rohan and 3 for maitri: "))
    retrive(b)
    print("Hello dear customer.")
    # /hello world for the first time in the new universe of the the new program
print("Hello world for the first time in the new era of the coding industry for the absolute begginers for the most of the time to do a new job for the other compiler to do a new job.")