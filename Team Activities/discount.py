"""
filename: discount
author: Tanner Levi
assignment: L02 Prepare: Team Activity
"""

"""
assignment: Work as a team to write a Python program named discount.py that gets a customer's subtotal as input and gets 
the current day of the week from your computer's operating system. Your program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer's operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. 
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount 
amount if applicable, the sales tax amount, and the total amount due.

CORE:
Your program asks the user for the subtotal but does not ask the user for the day of the week. 
Your program gets the day of the week from your computer's operating system.

Your program correctly computes and prints the discount amount if applicable.

Your program correctly computes and prints the sales tax amount and the total amount due
"""
from datetime import datetime

discountRate = 0.10
salesTaxRate = 0.06

subtotal = float(input("Please enter the subtotal: "))

d = datetime.now()
day = datetime.weekday(d)

if subtotal >= 50 and (day == 1 or day == 2):
    discount = round(subtotal * discountRate, 2)
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount

salesTax = round(subtotal * salesTaxRate, 2)
print(f"Sales tax amount: {salesTax:.2f}")

total = subtotal + salesTax

print(f"Total: {total:.2f}")
