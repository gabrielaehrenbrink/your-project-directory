class Contacts():
    def __init__(self):
        self._contacts = {}


     
    def add_contact(self, contact):
#         #   Adds a contact to the list of contacts
        for name, number in contact.items():
            self._contacts[name] = number
        
    