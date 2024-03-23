name =["Ahmad", "Ali", "Rafay", "Abeer",]
# List of people to invite to dinner
for x in range(len(name)):
    if len(name) == 2:
     break
    else:
     print(f"I am sorry  {name[x]} that i can't invite you for a dinner party")
    name.pop(x)
    print(f"dear {name[x]} you are still invited to the dinner party ")
    del name[:]
    print(name)
