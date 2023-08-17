""" 
Title: StockWatch
Purpose: A tool to help with day trading
Author: Divya Prasad
"""

import time
from get_stock_prices import get_stock_data
from plyer import notification

def price_ceiling(current_price:float, user_stock:str) -> None:
    """
    This handles the price ceiling functionality
    """
    user_price_ceiling = float(input("Provide price ceiling: $"))
    user_notification_ceiling = input(
        f"Would you like to be notified when the price surpasses ${user_price_ceiling:.2f} USD? (Y/N): "
    )
    if user_notification_ceiling.upper() == "Y":
        while True:
            try:
                current_price = float(get_stock_data(user_stock)[0])
            except Exception:
                print('Error fetching data. Retrying...') #fail safe if there is an issue in retrieving stock data
                time.sleep(60)
                continue
                
            if current_price > user_price_ceiling:
                title = f'{user_stock.upper()} stocks ROSE'
                message = f'{user_stock.upper()} stock rose above ${user_price_ceiling:.2f} USD to ${current_price:.2f} USD!'
                notification.notify(title=title, message=message)
                break
            time.sleep(90) #refreshes the current price every 1 min 30s
    elif user_notification_ceiling.upper() == "N":
        print("No worries, have a good day!")
    else:
        print("Invalid command")   
                
def price_floor(current_price: float, user_stock:str) -> None:
    """
    This handles the price floor functionality
    """
    user_price_floor = float(input("Please provide price floor: $"))
    user_notification_floor = input(
        f"Would you like to be notified when the price drops below ${user_price_floor:.2f} USD? (Y/N): "
    )
    
    if user_notification_floor.upper() == "Y":
        while True:
            try:
                current_price = float(get_stock_data(user_stock)[0])
            except Exception:
                print('Error fetching data. Retrying...') #fail safe if there is an issue in retrieving stock data
                time.sleep(60)   
                continue
            if current_price < user_price_floor:
                title = f'{user_stock.upper()} stocks DROPPED'
                message = f'{user_stock.upper()} stock dropped below ${user_price_floor:.2f} USD to ${current_price:.2f} USD!'
                notification.notify(title=title, message=message)
                break  
            time.sleep(90) #refreshes the current price every 1 min 30s
    elif user_notification_floor.upper() == "N":
        print("No worries, have a good day!")
    else:
        print("Invalid command")    


def main():
    """
    This is the main function
    """
    #TO DO: Loop it such that if they enter the wrong command, it allows them to try again without restarting the program
    print('Welcome to StockWatch! This is a tool to help investors with day trading')
    while True:
        user_stock = input("Enter stock symbol: ") 
        
        if user_stock.upper() == "EXIT":
            print('Have a good day!')
            break
        
        try:
            current_price = float(get_stock_data(user_stock)[0])
        except Exception:
            print('Invalid stock symbol. Please try again.') #Exception handling 
        else:
            change_points = get_stock_data(user_stock)[1]
            change_percent = get_stock_data(user_stock)[2]
            
            print(f"Current price for {user_stock} is: ${current_price:.2f} USD. Its price difference is {change_points}, {change_percent}.")
            user_choice = input('Would you like to set a price ceiling, price floor, or none? ')
            
            #For price ceiling:
            if user_choice.upper() == "PRICE CEILING":
                price_ceiling(current_price, user_stock)
                break
            #For price floor:        
            elif user_choice.upper() == "PRICE FLOOR":
                price_floor(current_price, user_stock)
                break
            elif user_choice.upper() == "NONE":
                print('No worries, have a good day!')
                break
                
            else:
                print('Invalid command. Please try again')
        
if __name__ == '__main__':
    main()
