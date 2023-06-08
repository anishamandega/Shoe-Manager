# importing libraries
from tabulate import tabulate
from wasabi import Printer

# Create a printer object
printer = Printer()

# Print some formatted text
printer.text("""Welcome to the shoe inventory system! This program allows you to manage your shoe inventory with ease.
You can search for shoes, view all shoes, add new shoes, and more.
This user-friendly menu will guide you through all available options.I hope you find this program helpful and easy to use.
Let's get started!""", color="green")


# defined Shoe class
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # created get cost method
    def get_cost(self):
        return self.cost

    # created get quantity method
    def get_quantity(self):
        return self.quantity

    # created string method
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


# created an empty list
shoe_list = []


# created read shoes data
def read_shoes_data():
    # used a try except block
    while True:
        try:
            # used with open to open inventory txt file
            with open("inventory.txt", "r") as files:

                # used next function to skip the first line in the inventory txt
                next(files)

                # used a for loop to iterate through the files and the readlines method
                for lines in files.readlines():
                    lines1 = lines.strip().split(',')

                    country = lines1[0]
                    code = lines1[1]
                    product = lines1[2]
                    cost = int(lines1[3])
                    quantity = int(lines1[4])
                    shoe_data = Shoe(country, code, product, cost, quantity)

                    # appended the new data to the shoe list
                    shoe_list.append(shoe_data)
                return shoe_list
        except FileNotFoundError:
            print("The file is not found")

            # used exit to leave the code if the file is not found
            exit()


# created function to capture new shoes
def capture_shoes():
    while True:
        print("")
        printer.text("                     CAPTURE MENU                  ", color="pink")
        printer.text("--------------------------------------------------", color="cyan")
        printer.text("Please select one of the following options:")
        printer.text("1. continue to capture new shoe", color="yellow")
        printer.text("2. exit", color="yellow")
        printer.text("--------------------------------------------------", color="cyan")

        choice = input("Enter here:").lower()
        print("")
        if choice == "1":
            print('You have selected to add a new shoe')
            # used try except block incase user doesn't enter an integer or float
            while True:
                try:

                    # used with open to open inventory txt file and used a
                    with open("inventory.txt", "a") as file:

                        shoe_country = input("Please enter the country the shoe is from:").capitalize()
                        shoe_code = input("Please enter the code of the shoe:").upper()
                        shoe_name = input("Please enter the name of the shoe:").capitalize()
                        shoe_price = int(input('Please enter the price of the shoe:'))
                        shoe_quantity = int(input("Please enter the quantity of the shoe:"))

                        new_shoe = Shoe(shoe_country, shoe_code, shoe_name, shoe_price, shoe_quantity)

                        # appended new shoe to shoe list
                        shoe_list.append(new_shoe)
                        printer.good(f"The {new_shoe.product} has been captured")

                        print("")
                        printer.text(f"Shoe Name       : {shoe_name}", color="blue")
                        printer.text(f"Shoe Code       : {shoe_code}", color="blue")
                        printer.text(f"Shoe Cost       : {shoe_price }", color="blue")
                        printer.text(f"Shoe Country    : {shoe_country}", color="blue")
                        printer.text(f"Shoe Quantity   : {shoe_quantity}", color="blue")

                        file.write(
                            f"\n{new_shoe.country}, {new_shoe.code}, {new_shoe.product}, {new_shoe.cost}, {new_shoe.quantity}")
                        break
                except ValueError:
                    printer.warn("Invalid input, please try again")

        elif choice == "2":
            print("You have selected to go back to the main menu")
            break

        else:
            printer.warn("Invalid choice, please try again")


def view_all():

    print("Displaying all shoes in the inventory:\n")

    # created an empty list
    empty_shoe = []

    # used a for loop to iterate through the shoe list
    for shoe in shoe_list:
        shoes = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]

        # appended to my empty list
        empty_shoe.append(shoes)

    # created a list headers
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]
    table = tabulate(empty_shoe, headers=headers, tablefmt="github")
    print(table)


# created function for restocking the shoe
def re_stock():
    # used min and lambda function
    lowest_shoe = min(shoe_list, key=lambda shoes: shoes.quantity)

    # printed the name and amount of the shoe with the lowest quantity
    print(f"The {lowest_shoe.product} has the lowest quantity of {lowest_shoe.quantity}\n")

    while True:
        print("")
        printer.text("                     SEARCH MENU                  ", color="pink")
        printer.text("--------------------------------------------------", color="cyan")
        printer.text("Please select one of the following options:")
        printer.text("1. continue to search", color="yellow")
        printer.text("2. exit", color="yellow")
        printer.text("--------------------------------------------------", color="cyan")

        choice = input("Enter here:").lower()
        print("")

        if choice == "1":
            while True:
                try:
                    # asked user for input on how much they would like to restock
                    restock_amount = int(input("Please enter the amount you will be restocking: "))

                    # added the restocking amount to the lowest shoe quantity
                    lowest_shoe.quantity += restock_amount
                    printer.good(f"\n{restock_amount} {lowest_shoe.product} have been restocked")

                    # used with open to open txt file and write to it
                    with open("inventory.txt", "w") as file:
                        file.write("Country,Code,Product,Cost,Quantity\n")

                        # used a for loop to iterate through the shoe list
                        for shoe in shoe_list:
                            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

                except ValueError:
                    printer.warn("Invalid input, please try again")

                break

        elif choice == "2":
            print("You have selected to go back to the main menu")
            break

        else:
            print("You have selected an invalid choice, please try again")


# created function for when user wants to search for a shoe
def search_shoe():
    while True:
        print("")
        printer.text("                     SEARCH MENU                  ", color="pink")
        printer.text("--------------------------------------------------", color="cyan")
        printer.text("Please select one of the following options:")
        printer.text("1. continue to search", color="yellow")
        printer.text("2. exit", color="yellow")
        printer.text("--------------------------------------------------", color="cyan")

        choice = input("Enter here:").lower()
        print("")

        # used if statement for when user enters yes
        if choice == "1":
            # asked user to enter the code of the shoe they would like to search for
            shoes_code = input("Please enter the code of the shoe you would like to search:")

            # used a for loop to iterate through the shoe list
            for shoe in shoe_list:

                # used if statement to check if shoe code entered matches any of the shoes in the text file
                if shoe.code == shoes_code:
                    # printed the shoe with the matching shoe
                    print("")
                    printer.text("                  Search Results                ", color="green")
                    print("")
                    printer.text(f"Shoe Name       : {shoe.product}", color="blue")
                    printer.text(f"Shoe Code       : {shoe.code}", color="blue")
                    printer.text(f"Shoe Cost       : {shoe.cost}", color="blue")
                    printer.text(f"Shoe Country    : {shoe.country}", color="blue")
                    printer.text(f"Shoe Quantity   : {shoe.quantity}", color="blue")
                    break

            # used else statement incase user enters a code that doesnt exist
            else:
                printer.text(f"No shoe with code {shoes_code} was found", color="red")
        # used an else statement for when the user selected to cancel
        elif choice == "2":
            print("You have selected to go back to the main menu")
            break

        else:
            printer.warn("Invalid choice, please try again")


# created a function to calculate the value of each shoe
def value_per_item():
    print("You have selected to view the total value of each shoe\n")

    # used a for loop to iterate through the shoe list
    for index, shoe in enumerate(shoe_list, 1):
        # multiplied the cost and quantity of the shoes to get the value
        shoe_value = float(shoe.cost) * int(shoe.quantity)

        # printed the results
        print("")
        print(f"Shoe {index}")
        printer.text(f"Shoe Name       : {shoe.product}", color="blue")
        printer.text(f"Shoe Code       : {shoe.code}", color="blue")
        printer.text(f"Shoe Cost       : R {shoe.cost}", color="blue")
        printer.text(f"Shoe Country    : {shoe.country}", color="blue")
        printer.text(f"Shoe Quantity   : {shoe.quantity}", color="blue")
        printer.text(f"Shoe Value      : R {shoe_value}", color="blue")


# created a function to get the highest quantity of the  shoes
def highest_qty():
    print("\nYou have selected to view the shoe with the highest quantity\n")
    # used max,lambda and key function
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)

    # printed the shoe with the highest quantity
    print(f"The {highest_shoe.product} have the highest quantity")
    printer.text(f"THEY ARE NOW ON SALE !!! ", color="red")


read_shoes_data()
while True:

    print("")

    # printed the menu the user choices from
    printer.text("           SHOW INVENTORY MENU",         color="pink")
    printer.text("--------------------------------------", color="cyan")
    printer.text("1. shoe search", color="yellow")
    printer.text("2. restocking shoes", color="yellow")
    printer.text("3. shoe with highest quantity ", color="yellow")
    printer.text("4. view all shoes", color="yellow")
    printer.text("5. capture a new shoe", color="yellow")
    printer.text("6. each shoe value", color="yellow")
    printer.text("7. exit the shoe menu ", color="yellow")
    printer.text("---------------------------------------", color="cyan")

    print("")
    # asked user to input there choice here
    user_choice = input("Enter here:").lower()
    if user_choice == "1":

        # called the search_shoe functions
        search_shoe()

    elif user_choice == "2":

        # called the re_stock function
        re_stock()

    elif user_choice == "3":

        # called the highest_qty function
        highest_qty()

    elif user_choice == "4":

        # called the view_all function
        view_all()

    elif user_choice == "5":

        # called the capture_shoes function
        capture_shoes()

    elif user_choice == "6":

        # called the view_per_item function
        value_per_item()

    elif user_choice == "7":
        printer.text("You have select to exit the Shoe Inventory Menu", color="yellow")
        printer.text("Goodbye", color="yellow")
        exit()

    else:
        printer.warn("Invalid choice, please try again")


