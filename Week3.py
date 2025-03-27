def calculate_discount(price, discount_percent):
    return price
price = input("Enter the price of the item: ")
discount_percent = input("Enter the discount percentage: ")
final_price = int(price) - (int(price) * int(discount_percent) / 100)
print("The price after discount is: ", int(final_price))

if int(discount_percent) >= 20:
    print (int(final_price))
else:
    print(int(price))

    # Yes, you can rename a repository. If it's hosted on GitHub, follow these steps:
    # 1. Go to the repository on GitHub.
    # 2. Click on "Settings" in the repository menu.
    # 3. Under the "Repository name" section, type the new name and click "Rename".
    # Note: Renaming a repository changes its URL. Update any local clones or references to the new URL.
