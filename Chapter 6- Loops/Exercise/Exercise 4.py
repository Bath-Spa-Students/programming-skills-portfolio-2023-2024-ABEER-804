#Exercise 4: Deli
Sandwhich_orders=["Grilled Chicken","Club Sandwich","Grilled Cheese"]
Finished_Sandwhich=[]
while Sandwhich_orders:
    current_sandwhich= Sandwhich_orders.pop(0)
    print(f"Your order {current_sandwhich} Sandwhich.")
    Finished_Sandwhich.append(current_sandwhich)
print("\nAll sandwich made:")
for sandwich in Finished_Sandwhich:
     print(sandwich)