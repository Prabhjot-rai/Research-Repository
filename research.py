# print on display
print("Hello, mum!")
print("Hello, lyle!")

# Variables
x = 7
y = "Lyle"
print(x)
print(y)

x = 8
x = "john"
print(x)

# python lists
thislist = ["orange", "kiwi", "grape"]
print(thislist)

list1 = ["orange", "kiwi", "grape"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# python strings
for x in "orange":
  print(x) 

  b = "Hello, john!"
print(b[:10]) 

d = "Hello"
e = "roman"
f = d + e
print(f)

d = "Hello"
e = "marina"
f = d + " " + e
print(f)

age = 30
txt = "My name is robert, and I am {}"
print(txt.format(age))

#python booleans
print(9 > 8)
print(9 == 8)
print(9 < 8)

a = 400
b = 55
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  # python opertor
  print(10 + 10)

  # python lists
thislist = ["kiwi", "peach", "grape", "watermelon", "cherry"]
thislist.remove("peach")
print(thislist)

thislist = ["orange", "grape", "peach"]

thislist.append("mango")

print(thislist)

thislist = ["kiwi", "mango", "watermelon"]
thislist.pop(1)
print(thislist)

thislist = ["watermelon", "grape", "kiwi"]
del thislist[0]
print(thislist)

# python tuple 
thistuple = ("kiwi", "mango", "watermelon")
print(thistuple)

fruits = ("kiwi", "mango", "orange")

(green, yellow, orange) = fruits

print(green)
print(yellow)
print(orange)

thistuple = ("orange", "watermelon", "kiwi")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

fruits = ("mango", "watermelon", "kiwi")
mytuple = fruits * 3

print(mytuple)

x = ("mango", "watermelon", "grape")
y = list(x)
y[1] = "watermelon"
x = tuple(y)

print(x)

thistuple = ("pineapple", "orange", "watermelon")
for i in range(len(thistuple)):
  print(thistuple[i])

# python sets
thisset = {"orange", "peach", "grape"}

print("peach" in thisset)

thisset = {"grape", "orange", "watermelon"}

thisset.add("pineapple")

print(thisset)

thisset = {"kiwi", "watermelon", "peach"}

thisset.discard("watermelon")

print(thisset)

thisset = {"grape", "kiwi", "orange"}

for x in thisset:
  print(x)

  









