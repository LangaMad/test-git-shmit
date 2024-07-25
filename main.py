
# 4 принипа ооп 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def heritance(self):
        print("I am a person")


# object1 = Person("John", 30)
# object2 = Person("Alice", 25)
# object1.display_info()
# object2.display_info()

# name = "John"
# name.index("o")

# Наследование 

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def heritance(self):
        print("I am a student")
    
    def study(self):
        print("I am studying")


# object3 = Student("Bob", 20, 11)
# object3.display_info()
# object4 = Student("Alice", 22, 9)
# object4.display_info()

# Множественное наследование

# class A:
#     def method(self):
#         print("Method A")

# class B:
#     def method(self):
#         print("Method B")
        
# class C(A, B):
#     def method(self):
#         print("Method C")

# class D(C):
#     def method(self):
#         print("Method D")

# d = D()
# d.method()
# print(D.mro())


# Полиморфизм

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# rex = Dog("Rex")
# whiskers = Cat("Whiskers")
# rex.make_sound()
# whiskers.make_sound()


# Инкапсуляция

# class Car:
#     def __init__(self,name) -> None:
#         self.name = name
        
#     def __prava(self):
#         print('show prava')

# golf = Car('Golf')
# golf.__prava()



