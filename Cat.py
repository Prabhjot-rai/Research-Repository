class Cat:
    name: None
    age: None
    _isHappy: None

    # constructor
    def __init__(self, name, age, isHappy = True):
        self.name = name
        self.age = age
        self._isHappy = isHappy

    def sound(self):
        print("Meow")

    def display(self):
        print("*** CAT ***")
        print("name:", self.name)      
        print("age:", self.age)
        print("isHappy:", self._isHappy)

# child class
class DomesticCat(Cat):
    owner: None

    def __init__(self, owner, name, age, isHappy=True):
        super().__init__(name, age, isHappy)
        self.owner = owner

    def display(self):
        super().display()
        print("owner: ", self.owner)

class WildCat(Cat):

    def sound(self):
        print("Hissssssss")


# cat1 = Cat("Luna", 5, True)
# cat1.display()
# cat1.sound()

dc1 = DomesticCat("Prabhjot", "Any", 2, True)
dc1.display()
dc1.sound()

wc1 = WildCat("Luna", 10, False)
wc1.display()
wc1.sound()




        

