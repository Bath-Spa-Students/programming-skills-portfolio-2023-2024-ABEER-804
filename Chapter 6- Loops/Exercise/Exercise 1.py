#Exercise 1: Pizza Toppings
while True:
    #Taking input from customer for selection of topping & quitting once finished
    topping=input("Please Enter your desired toppings:")
    if topping=='quit':
        print("Thank you for ordering")
        break
    print(f"Adding {topping} to your pizza.")