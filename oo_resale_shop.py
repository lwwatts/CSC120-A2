from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, starter_inventory: list = []):
        self.inventory = starter_inventory

    # What methods will you need?
    def buy(self, new_comp: Computer):
        self.inventory.append(new_comp)

    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

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

    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            comp = self.inventory[item_id]
            comp.update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
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
