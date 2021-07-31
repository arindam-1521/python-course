a = int(input("Enter the first number here: "))
b = int(input("Enter the second number here: "))
n = int(input("Enter the number of rows you wand in your star pattern: "))
i = 0
while(a>b):
    while i<n+1:
        print("*" * i)
        i += 1
        
while(a<b):
    while i<n+1:
        print("*" * (n-i))
        i += 1
        
