
from TicketingSystem import *

if __name__=="__main__":
    ts = TicketSystem()

    while True:
        print()
        print("#### welcome to ticketing system ####")
        print("To display all tickets press 1 ")
        print("To enter new ticket press 2")
        print("To respond a ticket press 3")
        print("To reopened a ticket press 4")
        print("To display a statistics press 5")
        print("To exit menu press 0")
        choice = input("Enter your choice: ")

        if choice == "0":
            exit()
        elif choice == "1":
            ts.display_all_tickets()
        elif choice == "2":
            ts.add_new_ticket()
        elif choice == "3":
            ts.respond()
        elif choice == "4":
            ts.reopen()
