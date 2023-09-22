class Book:
    title = None
    quantity = 10
    price = 100
    author = 'john'
    pulisher_name = 'abc'

    def __init__(self, title, quantity, price, author_name):
        self.title = title
        self.quantity = quantity
        self.price = price
        self.author = author_name
    
    def display(self):
        print("Title:", self.title)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Author:", self.author_name)
    

b1 = Book("Dune", 10, 5.99, "John Someone");
b1.display()


     
        
            