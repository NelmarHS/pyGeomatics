# Notes on classes:

class Employee:
    # class variable - only available within the class
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        """
        __init__: initializing method (runs when the class instance is created)
        self: object instance of method __init__
        first, last, pay: instance variables (attributes)
        """
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


employee_1 = Employee('John', 'Doe', 10000)
"""
When employee_1 is called like ^, the instance employee_1 is created. In the employee clas, __init__ runs
and creates:
        employee_1.first = John
        employee_1.last = Doe
        employee_1.pay = 10000
        employee_1.email = John + '.' + Doe + '@gmail.com'
"""

employee_1_fullname = employee_1.fullname()  # instance option 1
employee_1_fullname = Employee.fullname(employee_1) # instance option 2
"""
option 1: instance.method
employee_1 is an instance of Employee, within Employee, the method constructs the full name and returns it.
By calling the instance and applying the full name method in it, the full name is saved in the local variable.

option 2: Class.Method(instance)
Another way of applying the fullname method to the instance "employee_1": 
"""

# option 1
Employee.raise_amount = 1.05
# option 2
employee_1.raise_amount = 1.05
"""
Class or instance variables can be changed by either:
option 1: Change it for the whole class (all instances)
option 2: Change it for a single instance (specific instances)
"""


# Printing class.method results
class Point(object):
    def __init__(self, xinit, yinit):
        self.x = xinit
        self.y = yinit

    def reflect_x(self):
        reflected_point_x = Point(self.x, - self.y)
        return reflected_point_x

# Reflected_point_x instance with object(Point(3, 5))
reflected_point_x = Point.reflect_x(Point(3, 5))

# To access a variable from within the instance, outside the instance:
# - instance_name.instance_variable_name - i.e. reflected_point_x.x
print(f"Reflected Point: ({reflected_point_x.x}, {reflected_point_x.y})")



# read txt files:
data = open("studentdata.txt")
lines = data.readlines()
