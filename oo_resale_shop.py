'''
    Filename: oo_resale_shop.py
 Description: contains the class ResaleShop, which has an inventory of computers, can buy computers,
              and can refurbish and sell computers in its inventory.
      Author: Lucy Watts
        Date: 7 February 2025

    I did not collaborate with anyone on this assignment.
'''

'''Adds access to the Computer class'''
from computer import Computer

class ResaleShop:

    # What attributes will it need?
    '''inventory: a list which stores the inventory of the resale shop'''
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    '''
    Constructs a new ResaleShop object and by default sets the inventory
    to a blank list, can optionally take a list of Computers and set this list
    as the inventory; does not print or return anything
    '''
    def __init__(self, starter_inventory: list[Computer] = []):
        self.inventory = starter_inventory

    # What methods will you need?
    '''
    Takes in a Computer object and appends that Computer to the inventory list;
    does not print or return anything
    '''
    def buy(self, new_comp: Computer):
        self.inventory.append(new_comp)

    '''
    Takes in an item_id (list index) and, if there is a Computer at that index in the 
    list, removes that Computer from the list and prints a "sold" message. 
    If there is no Computer at that index, prints an error message
    '''
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    '''
    Takes in an item_id (list index) and an optional operating system and, 
    if there is a Computer at that index, "refurbishes" the computer. If there is 
    not a Computer at that index, prints an error message. In refurbishment, 
    changes the price of the Computer based on the age of the computer. If an operating
    system string is provided, replaces the Computer's current operating system with the 
    new operating system
    '''
    def refurbish(self, item_id: int, new_os: str = None):
        if self.inventory[item_id] is not None:
            comp = self.inventory[item_id]
            year_made = comp.get_year_made()
            if year_made < 2000:
                comp.update_price(0)
            elif year_made < 2012:
                comp.update_price(250)
            elif year_made < 2018:
                comp.update_price(550)
            else:
                comp.update_price(1000)
            
            if new_os is not None:
                comp.update_os(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    '''
    Takes in an item_id (list index) and a new price and, if there is a 
    Computer at that list index, updates the current price of that
    Computer with the new price, or prints an error message if there is
    no Computer at that list index
    '''
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            comp = self.inventory[item_id]
            comp.update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    '''
    Prints all the items in the ResaleShop's inventory list if the list is 
    not empty, or prints an error message if the list is empty
    '''
    def print_inventory(self):
        if len(self.inventory) != 0:
            for item in self.inventory:
                print(f'Item ID: {self.inventory.index(item)} :', end="")
                item.print_computer()
        else:
            print("No inventory to display.")

# for testing purposes only
def main():
    pass

if __name__ == "__main__":
    main()
