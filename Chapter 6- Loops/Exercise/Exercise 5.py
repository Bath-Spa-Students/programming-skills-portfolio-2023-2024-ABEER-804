#Exercise 5: No Pastrami 
Sandwhich_orders=["Grilled Chicken","Club Sandwich","Grilled Cheese"]
print("Sorry,We run out of pastrami sandwhich.")
while 'pastrami' in Sandwhich_orders:
    Sandwhich_orders.remove('pastrami')
finished_sandwiches=[]
while Sandwhich_orders:
    current_sandwich=Sandwhich_orders.pop()
    if current_sandwich != 'pastrami':
        finished_sandwiches.append(current_sandwich)
print("Updated Sandwich orders:", Sandwhich_orders)
print("Finished Sandwiches:",finished_sandwiches)