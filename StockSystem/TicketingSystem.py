from Ticket import Ticket
class TicketSystem:
    Tickets = []
    next_id = 2000


    #constructor
    def __init__(self):

        new_ticket = Ticket(2001, "prabhjot", "PPK", "prabh@gmail.com", "No internet connection")
        self.Tickets.append(new_ticket)

        new_ticket = Ticket(2002, "Marina", "MMM", "m@gmail.com", "Printer is not working")
        self.Tickets.append(new_ticket)

        new_ticket = Ticket(2003, "Willam", "WLM", "wlm@gmail.com", "Password is not working")
        self.Tickets.append(new_ticket)

        new_ticket = Ticket(2004, "James", "JMS", "jms@gmail.com", "My pc is not turn on")
        self.Tickets.append(new_ticket)

        self.next_id = 2005

    # display all tickets
    def display_all_tickets(self):
        print( "/n*** list of tickets***")

        if len(self.Tickets) == 0:
            print("No tickets to show")

        for p in self.Tickets:
            p.display()

    # add new ticket to system
    def add_new_ticket(self):

        print( "\n*** Enter details of new ticket***")
        # input of ticket_id
        name = input("Enter the name:")
        if name == "":
            print("Incorrect name input")
            return
        
        # input of staff_id
        staff_id= input("Enter the staff ID:")
        if staff_id == "":
            print("Incorrect staffID input")
            return
        
        # input of email
        email= input("Enter the email:")
        if email == "":
            print("Incorrect email input")
            return
        
        # input of issue
        issue = input("Enter the issue:")
        if issue == "":
            print("Incorrect issue input")
            return
           
        # add ticket to list
        new_ticket = Ticket(self.next_id, name, staff_id, email, issue)
        self.Tickets.append(new_ticket)
        self.next_id += 1

    def respond(self):
        sel_ticket_id = int(input("Enter the ticket no: "))
        for t in self.Tickets:
            if t.ticket_id == sel_ticket_id:
                resp = input("Enter response: ")
                t.status = "CLOSED"
                t.respond = resp 
    
    def reopen(self):
        sel_ticket_id = int(input("Enter the ticket no: "))
        for t in self.Tickets:
            if t.ticket_id == sel_ticket_id:
                t.status = "SUMMITTED"


            



# ts = TicketSystem();
# ts.display_all_tickets()

# # ts.add_new_ticket()
# # ts.add_new_ticket()
# # ts.display_all_tickets()

# ts.respond()
# ts.display_all_tickets()


    

        