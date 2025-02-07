class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, desc: str, pro_type: str, cap: int, mem: int, os: str, year: int, val: int):
        self.description = desc
        self.processor_type = pro_type
        self.hard_drive_capacity = cap
        self.memory = mem
        self.operating_system = os
        self.year_made = year
        self.price = val

    # What methods will you need?
    def update_os(self, new_os: str):
        self.operating_system = new_os

    def update_price(self, new_price: int):
        self.price = new_price

    def get_year_made(self):
        return self.year_made
    
    # prints the information of each computer in a readable format 
    def print_computer(self):
        print(f"Description: {self.description}, processor type: {self.processor_type}, hard drive capacity: {self.hard_drive_capacity}, memory: {self.memory}, operating system: {self.operating_system}, year made: {self.year_made}, price: ${self.price}")

#for testing purposes only
def main():
    pass

if __name__ == "__main__":
    main()
