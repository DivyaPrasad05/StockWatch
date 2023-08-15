from get_stock_prices import get_stock_data

def main():

    user_stock = input("Enter stock symbol: ") # TO DO: Validate that the entered stock symbol is valid
    print(f"Current price for {user_stock} is: ${get_stock_data(user_stock)[0]} USD. Its price difference is {get_stock_data(user_stock)[1]}, {get_stock_data(user_stock)[2]}.")
    user_price_ceiling = input("Provide price ceiling: ")
    user_notification = input(
        f"Would you like to be notified when the price surpasses {user_price_ceiling}? (Y/N): "
    )
    
    if user_notification.upper() == "Y":
        # set up desktop notifications
        pass
    elif user_notification.upper() == "N":
        print("No worries, have a good day!")
    else:
        print("Invalid command")
        
if __name__ == '__main__':
    main()
