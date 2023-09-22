# class Product
from math import isnan
class Product:
    name: None
    price: None
    quantity: None
    weight = None

    # constructor
    def __init__(self, name, price, ):
        self.name = p_name
        self.price = p_price
        self.quantity = p_quantity

    def display(self):
        print("***** PRODUCT *****")
        print("name: ", self.name)
        print("price:", self.price)
        print("quantity:", self.quantity)
        print("")

cookie = Product("Chocolate cookie", 5.00, 100)
cookie.display()

milk = Product("Oat milk", 3.99, 12)
milk.display()