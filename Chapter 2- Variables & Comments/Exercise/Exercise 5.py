# Exercise 5: USB Shopper
usb_stick_price = 6
# Price of each USB stick
total_money = 50
# Total budget in pounds
usb_sticks = total_money//usb_stick_price
# Calculate how many USB sticks she can buy
remaining_money = total_money % usb_stick_price
print(f"The girl can buy {usb_sticks}USB sticks and will have £{remaining_money} left")
# Display the results