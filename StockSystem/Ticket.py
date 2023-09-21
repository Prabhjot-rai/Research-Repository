

class Ticket():

    # constructor
    def __init__(self, ticket_id, name, staff_id, email, issue):
        self.ticket_id = ticket_id
        self.creator_name = name
        self.staff_id = staff_id
        self.email = email
        self.issue = issue
        self.respond = "Not yet provided"
        self.status = "SUBMITTED"
    
    def display(self):
        print()
        print("====== TICKET ======")
        print("Ticket ID:", self.ticket_id)
        print("creator name:", self.creator_name)
        print("staff_id:", self.staff_id)
        print("email:", self.email)
        print("issue:",self.issue)
        print("respond:",self.respond)
        print("status:",self.status)
    


# t = Ticket(2001, "prabhjot", "PRK", "prabh@gmail.com", "No internet connection")
# t.display()

# t1 = Ticket(2002, "Marina", "MMMM", "m@gmail.com", "Printer is not working")
# t1.display()

# t2 = Ticket(2003, "William", "WLM", "wlm@gmail.com", "Password is not working")
# t2.display()

# t3 = Ticket(2004, "James", "JMS", "jms@gmail.com", "My pc is not turn on")
# t3.display()
