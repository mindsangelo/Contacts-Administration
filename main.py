import cmd
import datetime
from cmd import Cmd

class Contact:

    # Initializer / Instance Attributes
    def __init__(self, name, last_name, age, phone_number, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.visible = True
        date_of_creation = datetime

    def update_contact(self,contact):
        pass


class ContactList:

    #Initializer/ Instance Attributes
    def __init__(self):
        self.lis = []

    def add_to_list(self, contact):
        self.lis.append(contact)

    def update_list(self, pos, contact):
        self.lis.remove(self.lis[pos])
        self.lis.insert(pos, contact)
        print("Contact list updated")

    def hide_contact(self, pos):
        i=0
        for x in self.lis:
           if (i==pos):
               x.visible = False
               self.update_list(i,x)
           i+=1

    def list_contacts(self):
        i=0
        for x in self.lis:
            if (x.visible == True):
                print("{} {} {} {} {} {}" .format(i, x.name, x.last_name, x.age, x.phone_number, x.email))
                i+=1

    def sort_contact_list(self):
        pass

class user:

    #Initializer / Instance Attributes
    def __init__(self, name):
        self.name


class MyPrompt(cmd.Cmd):
    intro = 'Welcome to the Contacts Administration Shell. Type help or ? to list commands. \n'

    def __init__(self):
        self.my_contact_list = ContactList()
        super(MyPrompt, self).__init__()

    # Commands
    def do_create(self, line):
        print("Type contact data: name, last name, age, phone number, email")
        name = input("Enter name: ")
        last_name = input("Enter last name: ")
        age = input("Enter age: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter e-mail: " )
        new_contact = Contact(name, last_name, age, phone_number, email)
        self.my_contact_list.add_to_list(new_contact)
        print("Contact {} number {} created succesfuly".format(new_contact.name, new_contact.phone_number))

    def do_update_contact(self, line):
        self.my_contact_list.list_contacts()
        selection = int(input("Enter the number of the contact you want to update"))
        name = input("Enter name: ")
        last_name = input("Enter last name: ")
        age = input("Enter age: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter e-mail: " )
        new_contact = Contact(name, last_name, age, phone_number, email)
        self.my_contact_list.update_list(selection, new_contact)

    def do_hide_contact(self, line):
        self.my_contact_list.list_contacts()
        selection = int(input("Enter the number of the contact you want to hide: "))
        self.my_contact_list.hide_contact(selection)

    def do_list_contacts(self, line):
        self.my_contact_list.list_contacts()

    def do_quit(self):
        print("Quitting..")
        raise SystemExit

if __name__ == '__main__':
    MyPrompt().cmdloop()
