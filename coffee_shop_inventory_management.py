def print_item_details(item, item_stock, item_price):
    item_total_value = item_stock * item_price
    print(f"{item}: {item_stock} units x £{item_price:.2f} = £{item_total_value:.2f}")


def calculate_total_stock_value(stock, price):
    total_stock_value = 0
    for item, item_stock in stock.items():
        if item in price:
            item_price = price[item]
            total_stock_value += item_stock * item_price
        else:
            print(f"Error: Price information missing for item {item}")
    return total_stock_value


def check_stock_and_price(stock, price):
    for item, item_stock in stock.items():
        if item not in price:
            print(f"Error: Price information missing for item {item}")


def main():
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

    menu.sort()

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
    
    total_stock_value = calculate_total_stock_value(stock, price)
    print(f"\nTotal Stock Value: £{total_stock_value:.2f}")
    
    check_stock_and_price(stock, price)

if __name__ == "__main__":
    main()
