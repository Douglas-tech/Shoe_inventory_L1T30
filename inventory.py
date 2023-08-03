'''Compulsory Task
Follow these steps:
● Code a Python program that will read from the text file inventory.txt and perform the following on the data, to prepare for presentation to your managers:
o We’ve provided a template for you in a file named inventory.py.
o Inside this file, you will find a class named Shoe with the following attributes:
● country,
● code,
● product,
● cost, and
● quantity.
o Inside this class define the following methods:
▪ get_cost - Returns the cost of the shoes.
▪ get_quantity - Returns the quantity of the shoes.
▪ __str__ - This method returns a string representation of a class.
o Outside this class create a variable with an empty list. This variable will be used to store a list of shoes objects
o Then you must define the following functions outside the class:
▪ read_shoes_data - This function will open the file inventory.txt and read the data from this file, then create a
shoes object with this data and append this object into the shoes list. One line in this file represents data to create one object of shoes.
You must use the try-except in this function for error handling. Remember to skip the first line using your code.
▪ capture_shoes - This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside the shoe list.
▪ view_all - This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function.
Optional: you can organise your data in a table format by using Python’s tabulate module.
▪ re_stock - This function will find the shoe object with the lowest quantity, which are the shoes that need to be re-stocked.
Ask the user if they want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.
▪ seach_shoe - This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
▪ value_per_item - This function will calculate the total value for each item .
Please keep the formula for value in mind; value = cost * quantity. Print this information on the console for all the shoes.
▪ highest_qty - Write code to determine the product with the highest quantity and print this shoe as being for sale.
o Now in your main create a menu that executes each function above. This menu should be inside the while loop. Be creative!'''

from tabulate import tabulate

# Define the Shoe class


class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Return the cost of the shoe
        return self.cost

    def get_quantity(self):
        # Return the quantity of the shoe
        return self.quantity

    def __str__(self):
        # Return a string representation of the class
        return f"{self.product} ({self.code}): {self.quantity} available @ {self.cost} {self.country}"


# Define functions to read data from inventory.txt and append Shoe objects to shoe_list
def read_shoes_data(shoes_list):
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip the header row
            for line in file:
                data = line.strip().split(", ")  # split the line by comma and space
                country = data[0]  # extract country data from the line
                brand = data[1]  # extract brand data from the line
                model = data[2]  # extract model data from the line
                cost = float(data[3])  # extract cost data from the line and convert to float
                quantity = int(data[4])  # extract quantity data from the line and convert to integer
                shoes_list.append(Shoe(country, brand, model, cost, quantity))  # create Shoe object and add to the list
    except FileNotFoundError:
        print("Error: inventory file not found.")  # handle file not found error

# Create an empty list to store Shoe objects


shoe_list = []
read_shoes_data(shoe_list)


'''    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''


def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print(f"{product} ({code}) added successfully")

    # Write the shoe to the inventory file
    with open("inventory.txt", "a") as file:
        file.write(f"{country}, {code}, {product}, {cost}, {quantity}\n")


'''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

# Define function to view all shoes in shoe_list


def view_all():
    if shoe_list:
        headers = ["Product", "Code", "Quantity", "Cost", "Country"]
        data = [[shoe.product, shoe.code, shoe.quantity, shoe.cost, shoe.country] for shoe in shoe_list]
        print(tabulate(data, headers=headers))
    else:
        print("No shoes found in inventory")


'''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

# Define function to restock shoes with lowest quantity


def re_stock():
    if shoe_list:
        lowest_quantity = min(shoe_list, key=lambda x: x.quantity).quantity
        shoes_to_restock = [shoe for shoe in shoe_list if shoe.quantity == lowest_quantity]
        if shoes_to_restock:
            print("The following shoes need to be restocked:")
            for shoe in shoes_to_restock:
                print(shoe)
            answer = input(f"Do you want to restock {lowest_quantity} shoes? (y/n): ")
            if answer.lower() == "y":
                for shoe in shoes_to_restock:
                    shoe.quantity += lowest_quantity
                save_to_file()
                print(f"{lowest_quantity} shoes restocked successfully")
        else:
            print("All shoes are well-stocked")
    else:
        print("No shoes found in inventory")



'''def save_to_file(shoes_to_restock):
    # Read existing inventory data
    existing_data = []
    with open("inventory.txt", "r") as file:
        existing_data = file.readlines()

    # Update quantity for restocked shoes
    updated_data = []
    for line in existing_data:
        shoe_data = line.strip().split(", ")
        code = shoe_data[1]
        restocked_shoe = next((shoe for shoe in shoes_to_restock if shoe.code == code), None)
        if restocked_shoe:
            shoe_data[4] = str(restocked_shoe.quantity)
        updated_data.append(", ".join(shoe_data))

    # Save updated data back to the file
    with open("inventory.txt", "w") as file:
        file.writelines(existing_data[0])  # Write the header row
        file.writelines(updated_data)  # Write the updated shoe data'''



'''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

# Define function to search for a shoe by code


def search_shoe():
    code = input("Enter shoe code to search: ")
    found_shoes = [shoe for shoe in shoe_list if shoe.code == code]
    print("Found shoes:", found_shoes)
    if found_shoes:
        headers = ["Product", "Code", "Quantity", "Cost", "Country"]
        data = [[shoe.product, shoe.code, shoe.quantity, shoe.cost, shoe.country] for shoe in found_shoes]
        print(tabulate(data, headers=headers))
    else:
        print(f"No shoes found with code {code}")


'''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

# Define function to calculate value per item for all shoes


def value_per_item():
    shoe_inventory = {}
    for shoe in shoe_list:
        if shoe.product not in shoe_inventory:
            shoe_inventory[shoe.product] = {'quantity': 0, 'total_cost': 0}

        shoe_inventory[shoe.product]['quantity'] += shoe.quantity
        shoe_inventory[shoe.product]['total_cost'] += shoe.cost * shoe.quantity

    headers = ['Product', 'Quantity', 'Total Cost', 'Value per Item']
    data = []
    for product, values in shoe_inventory.items():
        quantity = values['quantity']
        total_cost = values['total_cost']
        value_per_item = total_cost / quantity if quantity != 0 else 0
        data.append([product, quantity, total_cost, value_per_item])

    print(tabulate(data, headers=headers))


'''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    # Sort the list of shoes by quantity in descending order
    sorted_shoes = sorted(shoe_list, key=lambda shoe: shoe.quantity, reverse=True)

    # Get the shoe with the highest quantity (first item in the sorted list)
    highest_qty_shoe = sorted_shoes[0]

    # Print the shoe as being for sale
    print(f"The {highest_qty_shoe.product} shoe is for sale with the highest quantity of {highest_qty_shoe.quantity}.")


'''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

# Main menu
while True:
    print("\n======= Shoe Inventory System =======")
    print("1. Read shoes data from file")
    print("2. Capture new shoe")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Show shoe with the highest quantity")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_shoes_data(shoe_list)
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "0":
        print("Thank you for using our Shoe Inventory System!")
        break
    else:
        print("Invalid choice! Please choose again.")
