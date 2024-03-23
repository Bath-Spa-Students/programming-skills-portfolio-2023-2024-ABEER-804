#Exercise 4: Rivers
Rivers = {
    # Making a dictionary containing there country & its names
    "Meuse" : "France",
    "Kura " : "Georgia, Azerbaijan",
    "Aras" : "Turkey"
}
for River, Country in Rivers.items():
    # Using loop to display sentence of each river
    print(f"The {River} river run through {Country}.")
print("\nRivers:")
# Using loop to display river name in the glossary
for river in Rivers.keys():
    print(river)
print("\nCountries:")
# Using loop to display name of country in the glossary
for Country in Rivers.values():
    print(Country)