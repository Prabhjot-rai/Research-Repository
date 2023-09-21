from Product import Product
class StockSystem:
    products = []
    last_id = 2000

    #constructor
    def __init__(self):

        new_product = Product(2001, "Peanut cookies", 5.99, 12, True)
        self.product_list.append(new_product)

        new_product = Product(2002, "Chocolate cookies", 5.99, 10,)
        self.product_list.append(new_product)

        new_product = Product(2003, "Apple pie", 3.50, 20, flase)
        self.product_list.append(new_product product)

    # display all tickets 
    def display_all_tickets(self):
        print( "/n*** list of tickets***")

        if len(self.product_list) == 0:
            print("No products to show")

        for p in self.product_list:
            p.display()
                

    # add new product to system
    def add_new_product(self):

        print( "*** Enter details of new product ***")
        # input of name
        name = input("Enter the name of the product:")
        if name == "":
            print(RED + "Incorrect name input" + RESET)
            return
        
        # input of price
        price = input("Enter the price:") 
        try:
            price = float(price)
        except:
            print(RED, price, "is incorrect number.", RESET)
            return

        # input of quantity
        quantity = input("Enter the quantity:") 
        try:
            quantity = int(quantity)
        except:
            print(RED, quantity, "is incorrect number.", RESET)
            return
        
        # add product to list
        new_product = Product(self.next_id, name, price, quantity)
        self.product_list.append(new_product)
        self.next_id += 1

            
