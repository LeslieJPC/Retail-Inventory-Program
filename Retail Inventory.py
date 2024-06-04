import pickle


class RetailItem:
    def __init__(self, item, description, units_in_inventory, price):
        self.item = item
        self.description = description
        self.units_in_inventory = units_in_inventory
        self.price = price

    
class CashRegister:
    def __init__(self):
        self.item_dict = {1: RetailItem("Item #1", "Jacket", 12,59.95),2: RetailItem("Item #2", "Designer Jeans", 40, 34.95),3: RetailItem("Item #1", "Shirt", 20, 24.95)}  # Initialize an empty list to store RetailItem objects

    def purchase_item(self, item_number):
        """
        Add a RetailItem object to the Cash Register's item dictionary.
        
        Args:
            retail_item (RetailItem): The RetailItem object to add to the dictionary.
        """
        if item_number in self.item_dict:
            retail_item = self.item_dict[item_number]
            self.show_item(retail_item)
        else:
            print("Invalid item number.")
        '''
        self.item_dict[retail_item.item] = retail_item'''

    def get_total(self):
        """
        Calculate and return the total price of all items in the Cash Register.
        
        Returns:
            float: The total price of all items.
        """
        total_price = sum(item.price for item in self.item_dict.values())
        return total_price

    
    def show_items(self):
        print("Items in Cash Register:")
        for item_number, retail_item in self.item_dict.items():
            self.show_item(retail_them)

    def clear(self):
        self.item_dict = {}  # Clear the Cash Register's item

    def load_items(self, filename):
        """
        Load the item dictionary from a file using pickle.

        Args:
            filename (str): The name of the file to load the data from.
        """
        try:
            with open(filename, "rb") as file:
                self.item_dict = pickle.load(file)
        except FileNotFoundError:
            self.item_dict = {}

    def save_items(self, filename):
        """
        Save the item dictionary to a file using pickle.

        Args:
            filename (str): The name of the file to save the data.
        """
        with open(filename, "wb") as file:
            pickle.dump(self.item_dict, file)    

def main():
    '''
    # Create instances of RetailItem and CashRegister
    item1 = RetailItem("Item #1", "Jacket", 12, 59.95)
    item2 = RetailItem("Item #2", "Designer Jeans", 40, 34.95)
    item3 = RetailItem("Item #3", "Shirt", 20, 24.95)
    '''

    cash_register = CashRegister()

    '''
    # Purchase items
    cash_register.purchase_item(item1)
    cash_register.purchase_item(item2)
    cash_register.purchase_item(item3)
    '''
    while True:
        print("\nAvailable Items: ")
        for item_number, retail_item in cash_register.item_dict.items():
            print(f"{item_number}. {retail_item.description}")
        print("Enter 'done' to Checkout")
        print("---")
        # Asks user to input items/check out
        item_selection = input("Select an Item Number (or enter 'done' to Checkout): ")
        
        # Check if the user wants to finish entering items

        if item_selection =='1' and '1' in cash_register.item_dict:
            if item_1 == cash_register.item_dict ['1']
                print(f"Item: {item_1.item}")
                print(f"Description: {item_1.description}")
                print(f"Units in Inventory: {item_1.units_in_inventory}")
                print(f"Price: ${item_1.price:.2f}")
        elif item_selection =='2' and '2' in cash_register.item_dict:
            if item_2 == cash_register.item_dict ['2']
                print(f"Item: {item_2.item}")
                print(f"Description: {item_2.description}")
                print(f"Units in Inventory: {item_2.units_in_inventory}")
                print(f"Price: ${item_2.price:.2f}")
        elif item_selection =='3' and '3' in cash_register.item_dict:
            if item_3 == cash_register.item_dict ['3']
                print(f"Item: {item_3.item}")
                print(f"Description: {item_3.description}")
                print(f"Units in Inventory: {item_3.units_in_inventory}")
                print(f"Price: ${item_3.price:.2f}")
        else:
            if item_selection.lower() == "done":
                break
##            item_number = int(item_selection)
##            cash_register.purchase_item(item_number)
##        description = input("Enter item description: ")
##        units_in_inventory = int(input("Enter units in inventory: "))
##        price = float(input("Enter item price: "))
##
##        
##    def show_items(self):
##        """Display data about the RetailItem objects stored in the Cash Register's item dictionary."""
##        print("Items in Cash Register:")
##        for item in self.item_dict.values():
##            print("Item: {retail_item.item}")
##        print(f"Description: {retail_item.description}")
##        print(f"Units in Inventory: {retail_item.unit_in_inventory}")
##        print(f"Price: ${retail_item.price:.2f}")
##        print("---")


##   ''' # Load previously saved items (if any)
##    cash_register.load_items("cash_register_items.pickle")'''

    # Display items in the Cash Register and calculate the total price
##    cash_register.show_items()
##    total_price = cash_register.get_total()
##    print(f"Total Price: ${total_price: .2f}")

    # Clear the Cash Register (if needed)
    cash_register.clear()
    
    # Save the item list when done
    cash_register.save_items("cash_register_items.pickle")
    
if __name__ == "__main__":
    main()
