
price = float(input("Enter the price of the item: "))
if price > 1000:
    discount_price = price * 0.80
    print(f"New price after 20% discount: {discount_price}")
elif 500 <= price <= 1000:
    discount_price = price * 0.90
    print(f"New price after 10% discount: {discount_price}")
else:
    print(f"No discount. The price is: {price}")
