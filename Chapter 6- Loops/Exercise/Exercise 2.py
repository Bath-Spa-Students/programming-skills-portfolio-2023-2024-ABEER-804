#Exercise 2: Movie Tickets
while True:
        age=int(input("Enter your age:"))
        if age==0:
            break
        elif age< 3:
            print("Your ticket is free")
        elif 3 <=age<=12:
             print("Your ticket coast is $10.")
        else:
             print("Your ticket coast is $15.")