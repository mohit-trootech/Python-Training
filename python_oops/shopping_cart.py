import json
import os


class ShoppingCart:
    """Python Class to Implement Shopping Cart Logic - Add Items, Print Items, Delete Items, Total Price"""

    def __init__(self, customer_name):
        self.__name = name
        self.__shopping_dictionary = {}
        self.__path = os.path.join(os.getcwd(), f"users_carts")
        if not ShoppingCart.load_data(self):
            self.__shopping_dictionary = {"Cart Owner": f"{customer_name} Cart"}
        print(*self.__shopping_dictionary.values(), "Successfully Created")

    def add_items(self, item_name, item_price, item_quantity):
        self.__shopping_dictionary.setdefault(f"Item {item_name} Details",
                                              {"item_name": item_name,
                                               "item_price": item_price,
                                               "item_quantity": item_quantity})

    def get_cart(self):
        items = [i for i in self.__shopping_dictionary.values()][1:]
        if not items == []:
            for i in items:
                print(f'Name: {i.get("item_name")} '
                      f', Price: {i.get("item_price")}',
                      f', Quantity: {i.get("item_quantity")}')
        else:
            print("First Add Some Items in Cart")

    def get_total_price(self):
        total_price = 0
        items = [i for i in self.__shopping_dictionary.values()][1:]
        if not items == []:
            for i in items:
                total_price += i.get("item_price") * i.get("item_quantity")
            print(f"Total Price of Cart: {total_price}")
        else:
            print("First Add Some Items in Cart")

    def save_data(self):
        with open(os.path.join(self.__path, f"{self.__name.lower()}_cart.json"), "w") as f:
            f.write(json.dumps(self.__shopping_dictionary, indent=4))
            print("File Saved Successfully at {}".format(self.__path))

    def load_data(self):
        try:
            with open(os.path.join(self.__path, f"{self.__name.lower()}_cart.json"), "r") as f:
                x = f.read()
                self.__shopping_dictionary = json.loads(x)
                return True
        except FileNotFoundError:
            return False

    def remove_file(self):
        try:
            os.remove(f"{self.__name.lower()}_cart.json")
        except FileNotFoundError:
            print("File Not Exist")


print("Shopping Cart Implementation using Class \nPress C/c to Stop")
name = input("Enter Your Name: ")
p_obj = ShoppingCart(name)
while True:
    options = input("Enter Your Choice\n"
                    "1. Add Items\n"
                    "2. Cart Details\n"
                    "3. Cart Total\n"
                    "4. Save Cart Details\n"
                    "5. Delete Saved Details: ")
    if options == "1":
        print("Start Adding Items in Cart")
        while True:
            item_name = input("Enter Item Name: ")
            try:
                item_price = float(input("Enter Price: "))
                item_quantity = float(input("Enter Quantity: "))
                p_obj.add_items(item_name, item_price, item_quantity)
                print("Item Added Successfully")
                stop_adding_items = input("Press C/c to Stop Entering New Items Else Press Any Key: ")
                if stop_adding_items.lower() == "c":
                    break
            except ValueError:
                print("Enter Item Price and Quantity in Correct Format ie. 24/3.5/99.99")
    elif options == "2":
        p_obj.get_cart()
    elif options == "3":
        p_obj.get_total_price()
    elif options == "4":
        p_obj.save_data()
    elif options == "5":
        p_obj.remove_file()
    elif options.lower() == "c":
        print("Thanks for Using")
        exit()
    else:
        print("Try Again With Valid Input")
