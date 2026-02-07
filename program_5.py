# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

TAX_RATE = 0.07

# Get hot dog type
print("Hot Dog Menu")
print("1. Hot Dog ($3.50)")
print("2. Chili Dog ($4.50)")

choice = input("Enter 1 or 2: ")

# Set base price
if choice == "1":
    cost = 3.50
elif choice == "2":
    cost = 4.50
else:
    print("Invalid choice.")
    exit()

# Optional toppings
cheese = input("Add cheese for $0.50? (y/n): ")
if cheese.lower() == "y":
    cost += 0.50

peppers = input("Add peppers for $0.75? (y/n): ")
if peppers.lower() == "y":
    cost += 0.75

onions = input("Add grilled onions for $1.00? (y/n): ")
if onions.lower() == "y":
    cost += 1.002

 # Author: Dre Dre
# Date: February 6, 2026
# Title: Hot Dog Order Program
#
# Flowchart:
# START
#    |
#    v
# Display Hot Dog Menu
#    |
#    v
# Input: Hot Dog type (1 or 2)
#    |
#    v
# Is choice valid? ----No----> Display "Invalid choice" --> END
#    |
#    Yes
#    |
#    v
# Set base price (Hot Dog $3.50 / Chili Dog $4.50)
#    |
#    v
# Input: Add cheese? (y/n)
#    |
#    v
# Yes ---> Add $0.50 to cost
# No ----> Skip
#    |
#    v
# Input: Add peppers? (y/n)
#    |
#    v
# Yes ---> Add $0.75 to cost
# No ----> Skip
#    |
#    v
# Input: Add grilled onions? (y/n)
#    |
#    v
# Yes ---> Add $1.00 to cost
# No ----> Skip
#    |
#    v
# Calculate tax (cost * 0.07)
#    |
#    v
# Calculate total (cost + tax)
#    |
#    v
# Display: Hot dog cost, Tax, Total cost
#    |
#    v
# END