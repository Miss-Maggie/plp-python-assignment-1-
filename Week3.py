def calculate_discount(price, discount_percent):
    return price
price = input("Enter the price of the item: ")
discount_percent = input("Enter the discount percentage: ")
final_price = int(price) - (int(price) * int(discount_percent) / 100)
#print("The price after discount is: ", int(final_price))

if int(discount_percent) >= 20:
    print (int(final_price))
else:
    print(int(price))


   