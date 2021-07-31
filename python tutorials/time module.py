import time

initial = time.time()
# print(initial)
j = 0
while j < 45:
    print("Joy is a student.")
    time.sleep(.1) #The sleep function waits for the certain time then run or executes the programm file for the first time.
    j = j + 1
print("while loop ran in ", time.time() - initial)

initial2 = time.time()
for i in range(45):
    print("Joy is a very good boy.")
print("for loop ran in ", time.time() - initial2)
print("loop is finished.")


local_time = time.asctime(time.localtime(time.time()))
print(local_time)
