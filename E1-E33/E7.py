## Sum of first n positive integers ##

# Get positive integer from user
integer = int(input("Pick a positive number:"))

# Creat Sum
sum = int((integer * (integer +1))/2)

#return sum
print("The result of the sum of the first {} positive integers is: {}".format(integer, sum))