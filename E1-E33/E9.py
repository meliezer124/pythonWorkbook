## Compound Interest ##

## Amount deposited
deposit = float(input("Please deposit amount:"))

## Calculate amount by years
one_year = deposit + (deposit * 0.04)
two_year = one_year + (one_year * 0.04)
three_year = two_year + (two_year * 0.04)

# Display results
print("After one year, the amount in your account will be: ${0:.2f}".format(one_year))
print("After two years, the amount in your account will be: ${0:.2f}".format(two_year))
print("After three years, the amount in your account will be: ${0:.2f}".format(three_year))

