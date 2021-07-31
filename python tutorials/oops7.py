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
            f"The name is {self.name},salary is {self.salary}, standard is {self.role}"
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
        print("This is good", string)


class Programmer(Employee):
    def __init__(self, aname, asalary, arole,languages):
        
        
        
    def printprog(self):
        return f"The Progarmmer's name is {self.name},salary is {self.salary}, standard is {self.role}"


harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 333, "Teacher")
shubham = Programmer("Shubham", 888, "Programmer")
karan = Programmer("Karan", 1210, "developer")
print(karan.printprog())
