#Exercise 4: Rivers
Rivers = {
    "Meuse" : "France",
    "Kura " : "Georgia, Azerbaijan",
    "Aras" : "Turkey"
}
for River, Country in Rivers.items():
    print(f"The {River} river run through {Country}.")
print("\nRivers:")
for river in Rivers.keys():
    print(river)
print("\nCountries:")
for Country in Rivers.values():
    print(Country)