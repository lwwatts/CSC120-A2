'''
    Filename: computer.py
    Description: contains the class Computer, which holds all the information for a Computer object and can update
        the Computer as necessary.
    Author: Lucy Watts
    Date: 7 February 2025

    I did not collaborate with anyone on this assignment.
'''

class Computer:

    # What attributes will it need?
    '''description: a string naming the computer's model'''
    description: str
    '''processor_type: a string naming type of processor this computer has'''
    processor_type: str
    '''hard_drive_capacity: the numerical capacity of the computer's hard drive (units not specified)'''
    hard_drive_capacity: int
    '''memory: the size of the computer's memory (units not specified)'''
    memory: int
    '''operating_system: a string naming the computer's operating system'''
    operating_system: str
    '''year_made: the year the computer was made'''
    year_made: int
    '''price: the price of the computer in US dollars'''
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    '''
    Constructs a new Computer object given the components of a computer: description, processor type,
    hard drive capacity, memory, operating system, year made, and price; does not print or return anything
    '''
    def __init__(self, desc: str, pro_type: str, cap: int, mem: int, os: str, year: int, val: int):
        self.description = desc
        self.processor_type = pro_type
        self.hard_drive_capacity = cap
        self.memory = mem
        self.operating_system = os
        self.year_made = year
        self.price = val

    # What methods will you need?

    '''
    Takes a new operating system string and replaces the current operating system
    with the new one; does not print or return anything
    '''
    def update_os(self, new_os: str):
        self.operating_system = new_os

    '''
    Takes in a new price and replaces the current price with the new one;
    does not print or return anything
    '''
    def update_price(self, new_price: int):
        self.price = new_price

    '''
    Takes no inputs, returns the year the computer was made
    '''
    def get_year_made(self):
        return self.year_made
    
    '''
    Takes no inputs, prints the information contained in the Computer in a readable format
    '''
    def print_computer(self):
        print(f"Description: {self.description}, processor type: {self.processor_type}, hard drive capacity: {self.hard_drive_capacity}, memory: {self.memory}, operating system: {self.operating_system}, year made: {self.year_made}, price: ${self.price}")

#for testing purposes only
def main():
    pass

if __name__ == "__main__":
    main()
