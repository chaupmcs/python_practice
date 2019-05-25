"""
    (x,y) = (y,x): cacl from the right handed side first. AFter that, calc on the left.
"""

class Person():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return "name = {}, age = {}, salary = {}".format(self.name, self.age, self.salary)


x, y = 2, 3
peter, alex = Person("Peter", 20, 10), Person("Alex", 22, 13)
print("BEFORE SWAP:")
print("x", x)
print("y", y)
print("peter", peter)
print("alex", alex)

x, y = y, x
peter, alex = alex, peter
print("AFTER SWAP:")
print("x", x)
print("y", y)
print("peter", peter)
print("alex", alex)



print("----------")
x, y = 2, 3
x = x + y
y = x - y
x = x - y
print(x, y)