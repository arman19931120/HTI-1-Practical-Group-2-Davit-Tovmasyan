import math



class Employee:
    def __init__(self, first_name, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name

    def __repr__(self):
        return f'<Employee first_name={self.first_name}>'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# emp1 = Employee('John', 'James')
# emp2 = Employee('A', 'B')

# print(emp1.full_name())
# print(emp2.full_name())


class User:
    def __init__(self, first_name, last_name, email, username, password):
        pass



class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def __eq__(self, other):
        return self.radius == other.radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius


c1 = Circle(4)

c2 = Circle(6)
# c2 = Circle(9)


print(c1.perimeter)
print(c1.perimeter)
print(c1.perimeter)
print(c1.area)
print(c2.perimeter)



