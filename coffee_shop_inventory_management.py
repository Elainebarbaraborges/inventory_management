def print_item_details(item, item_stock, item_price):
    """
    Print the details of an item including its stock and total value.

    Args:
        item (str): The name of the item.
        item_stock (int): The stock quantity of the item.
        item_price (float): The price of the item.

    Returns:
        None
    """
    item_total_value = item_stock * item_price
    print(f"{item}: {item_stock} units x £{item_price:.2f} = £{item_total_value:.2f}")


def calculate_total_stock_value(stock, price):
    """
    Calculate the total value of the stock.

    Args:
        stock (dict): A dictionary containing item names and their respective stock quantities.
        price (dict): A dictionary containing item names and their respective prices.

    Returns:
        float: The total value of the stock.
    """
    total_stock_value = 0
    for item, item_stock in stock.items():
        if item in price:
            item_price = price[item]
            total_stock_value += item_stock * item_price
        else:
            print(f"Error: Price information missing for item {item}")
    return total_stock_value


def check_stock_and_price(stock, price):
    """
    Check for any inconsistencies between stock and price dictionaries.

    Args:
        stock (dict): A dictionary containing item names and their respective stock quantities.
        price (dict): A dictionary containing item names and their respective prices.

    Returns:
        None
    """
    for item, item_stock in stock.items():
        if item not in price:
            print(f"Error: Price information missing for item {item}")


def main():
    # Define the menu items
    menu = ["Latte", 
            "Mate Tea", 
            "Cappuccino", 
            "Americano", 
            "White Americano", 
            "Espresso", 
            "Hot Chocolate", 
            "Chai Latte", 
            "Mocha", 
            "Macchiato",
            "Breakfast Tea", 
            "Green Tea", 
            "Peppermint Tea"]
    
    # Define stock quantities for each item
    stock = {"Latte": 200, 
             "Mate Tea": 317, 
             "Cappuccino": 130, 
             "Americano": 318, 
             "White Americano": 214, 
             "Espresso": 123, 
             "Hot Chocolate": 230, 
             "Chai Latte": 190, 
             "Mocha": 228, 
             "Macchiato": 141, 
             "Breakfast Tea": 120, 
             "Green Tea": 78, 
             "Peppermint Tea": 93}

    # Define prices for each item
    price = {"Latte": 10.20, 
             "Mate Tea": 16.20, 
             "Cappuccino": 10.20, 
             "Americano": 9.80, 
             "White Americano": 9.80,
             "Espresso": 8.80, 
             "Hot Chocolate": 10.20, 
             "Chai Latte": 9.80, 
             "Mocha": 7.60, 
             "Macchiato": 8.80, 
             "Breakfast Tea": 8.20, 
             "Green Tea": 8.20, 
             "Peppermint Tea": 8.20}

    # Sort the menu items alphabetically 
    menu.sort()

    # Print details for each item in the menu    
    for item in menu: 
        if item in stock:
            item_stock = stock[item]
            if item in price:
                item_price = price[item]
                print_item_details(item, item_stock, item_price)
            else:
                print(f"Error: Price information missing for item {item}")
        else:
            print(f"Error: Stock information missing for item {item}")
    
    # Calculate and print the total stock value
    total_stock_value = calculate_total_stock_value(stock, price)
    print(f"\nTotal Stock Value: £{total_stock_value:.2f}")
    
   # Check for inconsistencies between stock and price dictionaries
    check_stock_and_price(stock, price)


if __name__ == "__main__":
    main()
