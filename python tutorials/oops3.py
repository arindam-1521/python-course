class Employee:
    no_of_leaves = 3  # This is same for all the elements of the list.
    def __init__(self,aname,asalary,arole): #This is a constructor.the class takes argument after running the function.
        self.name = aname
        self.salary = asalary
        self.role = arole
        

    def printdetails(self):
        return (f"The name is {self.name},salary is {self.salary}, standard is {self.std}")


harry = Employee("Harry",455,"Instructor")
# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 23000
# harry.std = 12

# rohan.name = "Rohan"
# rohan.salary = 12000
# rohan.std = 11
# print(rohan.printdetails())
print(harry.salary)
print(harry.name)
# print(rohan.no_of_leaves)

