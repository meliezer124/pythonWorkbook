## Tax and Tip ##

#Cost of meal#
base_cost = float(input("What was the cost of your meal?"))

# Calculating Tax and Tip
tip = base_cost * 0.18
tax = base_cost * 0.0761

# Total cost
total_cost = tip + tax + base_cost

# Output
print("Your tip for this meal is: ${0:.2f}".format(tip))
print("Your tax for this meal is: ${0:.2f}".format(tax))
print("Your total for this meal with tax and tip comes out to: ${0:.2f}".format(total_cost))

