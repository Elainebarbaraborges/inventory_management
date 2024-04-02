Read me file: 

# Coffee Shop Inventory Management System
This Python script manages the inventory stock and prices for a coffee shop. It includes functions to print item details, calculate total stock value, and check for inconsistencies between stock and price information.

## Clone
To clone this repository, run the following command:
~~~
https://github.com/Elainebarbaraborges/coffee_shop_inventory.git
~~~

## Functions
print_item_details(item, item_stock, item_price)

Prints the details of an item including its stock quantity and price per unit.


## Parameters for print_item_details Function:
- `item` (str): The name of the item.
- `item_stock` (int): The stock quantity of the item.
- `item_price` (float): The price of the item.

Returns: None


## Parameters for calculate_total_stock_value Function:
- `stock` (dict): A dictionary containing item names as keys and their respective stock quantities as values.
- `price` (dict): A dictionary containing item names as keys and their respective prices as values.

Returns: float - The total value of the stock. This function iterates over the `stock` dictionary, retrieves the corresponding price for each item from the `price` dictionary, and calculates the total value by multiplying the stock quantity with the price for each item.

## Parameters for check_stock_and_price Function:
- `stock` (dict): A dictionary containing item names as keys and their respective stock quantities as values.
- `price` (dict): A dictionary containing item names as keys and their respective prices as values.

Returns: None

main()

The main function initializes the inventory stock and price dictionaries, sorts the menu items alphabetically, displays item details, calculates the total stock value, and checks for any inconsistencies.

## Usage
Run the script inventory_management.py.

The script will display item details, total stock value, and any inconsistencies found.

## Sample Data
The script comes with sample data for menu items, their stock quantities, and prices. You can modify this data according to your needs.

## Dependencies
This script has no external dependencies.

## Error Handling
The script includes basic error handling for missing price or stock information. It will print appropriate error messages if any inconsistencies are found.

