def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Ask the user for the original price
price_input = float(input("Enter the original price of the item: "))

# Ask the user for the discount percentage
discount_input = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price_input, discount_input)

# Print the result
if discount_input >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")