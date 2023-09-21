# python dictionaries
thisdict =	{
  "brand": "Toyoto",
  "model": "Fortuner",
  "year": 2004
}
x = thisdict["model"]
print(x)

thisdict = {
  "brand": "Toyota",
  "model": "Fortuner",
  "year": 2004
}
thisdict.update({"year": 2021})

print(thisdict)

thisdict =	{
  "brand": "Evoque",
  "model": "Range rover",
  "year": 1970
}
thisdict["color"] = "black"
print(thisdict)

thisdict =	{
  "brand": "Maruti Suzuki",
  "model": "Swift",
  "year": 2004
}
del thisdict["model"]
print(thisdict)

thisdict =	{
  "brand": "Mercedes",
  "model": "BMW",
  "year": 1928
}
for x in thisdict:
  print(x)

# python while loops
i = 2
while i < 8:
  print(i)
  if (i == 4):
    break
  i += 2

  # python fuctions
def my_function():
   print("Hello from a function")

my_function()

# python lambda
x = lambda a: a + 10
print(x(15))

x = lambda a, b: a * b
print(x(5, 8))

x = lambda a, b, c: a + b + c
print(x(6, 4, 6))

# python arrays
cars = ["Toyoto", "Evoque", "BMW"]

x = cars[0]

print(x)

cars = ["Maruti Suzuki", "Ford", "Audi"]

x = len(cars)

print(x)

cars = ["Audi", "Honda", "Toyoto"]

cars.append("Porsche")

print(cars)

cars = ["Honda", "Porsche", "Toyoto"]

cars.pop(1)

print(cars)

# python classes/objects
class MyClass:
  x = 10

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("William", 40)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("William", 40)
p1.myfunc()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("William", 40)

p1.age = 50

print(p1.age)

# python inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("David", "Robert")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("John", "Helen keller")
x.printname()

