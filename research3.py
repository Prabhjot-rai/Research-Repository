# python iterators
mytuple = ("peach", "orange", "strawberry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "cherry"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# python scope
def myfunc():
  x =400 
  print(x)

myfunc()

x = 500

def myfunc():
  print(x)

myfunc()

print(x)
x = 400

def myfunc():
  x = 300
  print(x)

myfunc()

print(x)

x = 500

def myfunc():
  global x
  x = 300

myfunc()

print

# python date 
import datetime

x = datetime.datetime(2021, 3, 19)

print(x)

import datetime

x = datetime.datetime(2020, 9, 3)

print(x.strftime("%B"))

 # python math
x = min(10, 20, 35)
y = max(10, 20, 35)

print(x)
print(y)

x = pow(6, 3)

print(x)

# python JSON
import json

# some JSON:
x = '{ "name":"Thomas", "age":45, "city":"New Zealand"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])




