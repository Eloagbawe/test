def f(x):
    f.counter = getattr(f, "counter", 0) + 1
    print(f.counter)
    return "Monty Python"
# for i in range(10):
#     f(i)
# f(5)
# f(6)
# f(6)
# x = f.counter + 25
# # print(f.counter)
# print(x)

class Person:

    def __init__(self,name, age ="23"):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name

shola = Person("shola", 27)

# print(shola.getName())
# print("Hello")
# print(shola.age)

class Robot:
    def __init__(self, name):
        self.name = name
        print(name + " has been created!")

    def __del__(self):
        print(self.name + " has been destroyed")

x = Robot("Tik-Tok")
y = Robot("Jenkins")
#z = x

print("Deleting x")
del x
print("Deleting z")
#del z
del y
#print(y.name)