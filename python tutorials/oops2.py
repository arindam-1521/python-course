class Employee:
    no_of_leaves = 3 #This is same for all the elements of the list.
    pass


harry = Employee()
rohan = Employee()
harry.name = "Harry"
harry.salary = 23000
harry.std = 12
rohan.name = "Rohan"
rohan.salary = 12000
rohan.std = 11
print(harry, rohan)
print(harry.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 34
print(rohan.__dict__)
print(Employee.__dict__)
print(Employee.no_of_leaves)
print(harry.name)