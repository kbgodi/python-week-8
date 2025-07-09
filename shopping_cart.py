
# Create a shopping cart programme that will contionualy ask the user for a food product and the price of that product
# Have an exist clause if the user wishies to stop adding more things to their cart
# At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit:")
    if food.lower == "q":
        break
    else:
        price = float(input("Enter the price of the {food: R}"))
        foods.append(food)
        prices.append(price)
        
        print("=====YOUR CART=====")
        
        for food in prices:
            print(food, end= " ")
            
        for price in prices:
            total  += price
            
        print("/")
        print(f"Your total is: R{total}")

 