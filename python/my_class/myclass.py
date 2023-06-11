class MyClass:
    x=7
print(MyClass)

class student:
  def __init__(self, name, id):
    self.name = name
    self.id = id
p1 = student("John", 3678)
print(p1.name)
print(p1.id)

# without __str__
class student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = student("senthil", 36)
p1.myfunc()


# prints a greeting
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("The animal speaks.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        print("Meow!")

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

# Calling methods
animal.speak()  # The animal speaks.
dog.speak()     # Woof! Woof!
cat.speak()     # Meow!



