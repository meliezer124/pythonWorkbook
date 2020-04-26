## Bottle Deposits ##

# Get amount of each type
liter_or_less = float(input("How many containers do you have that hold a liter or less?"))
more_than_liter = float(input("How many containers do you have that hold more than a liter?"))

#Calculate invididual typed deposits
amt_less = liter_or_less * 0.10
amt_more = more_than_liter * 0.25

# Calculate total deposit
deposit = amt_less + amt_more

# return deposit
print("Your refund for these bottles is : ${0:.2f}".format(deposit)) #{0:.2f} is what limits the float to 2 places!