class Employee:
    no_of_leaves = 3  # This is same for all the elements of the list.

    def __init__(
        self, aname, asalary, arole
    ):  # This is a constructor.the class takes argument after running the function.
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return (
            f"The name is {self.name},salary is {self.salary}, standard is {self.std}"
        )

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This is good",string)


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 333, "Teacher")
karan = Employee.from_str("Karan-400-student")
# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 23000
# harry.std = 12

# rohan.name = "Rohan"
# rohan.salary = 12000
# rohan.std = 11
# print(rohan.printdetails())
# print(harry.salary)
# print(harry.name)
# print(rohan.no_of_leaves)
# harry.change_leaves(12)
# rohan.change_leaves(99)
# print(harry.no_of_leaves)
# print(rohan.no_of_leaves)
# print(Employee.no_of_leaves)
print(karan.salary)
print(karan.no_of_leaves)
print(karan.printgood("Rohan"))
print(Employee.printgood("Harry"))
print(karan.salary)
print(Employee.no_of_leaves)
print("Hello world for the first time to do a new job so there is a new job for the development of the new so to do a new for the crative to do a new system for the most of the new so there")
