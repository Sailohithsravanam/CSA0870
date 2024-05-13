
fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day old loaves purchased: "))
price_per_loaf = 185
regular_price = price_per_loaf * fresh_loaves
discount = price_per_loaf * 0.6 * day_old_loaves
total_price = regular_price + discount
print(f"Regular price: Rs. {regular_price:.2f}")
print(f"Amount of new loaves: {price_per_loaf * fresh_loaves:.2f}")
print(f"Amount of day old loaves: {discount:.2f}")
print(f"Total amount: Rs. {total_price:.2f}")