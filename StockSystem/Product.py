from data import *

# Product class
class Product():
    # product_id: None
    # name: None
    # price: None
    # quantity: None
    # __status: None

    # constructor
    def __init__(self, product_id, name, price, quantity, status = True):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.status = status


        # display
        def display(self):
            print("***PRODUCT***")
            print("ID:", self.product_id)
            print("price:$", self.price)
            print("quantity:", self.quantity)
            if self.__status:
                print(Green + "ACTIVE" + RESET)
            else:
                 print(RED + "ARCHIVE" + RESET)
    #cost calculation
    def cost(self):
        return self.price * self.quantity

    # getter
    def get_status(self):
        return self      
            
            

