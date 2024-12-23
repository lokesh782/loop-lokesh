
price = float(input("Enter the price of the item: "))
if price > 1000:
    discount = 0.10  
elif price > 500:
    discount = 0.05 
else:
    discount = 0  

final_price = price - (price * discount)
print(f"The final price is: {final_price}")
