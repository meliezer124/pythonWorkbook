## Faces on Money

# Book-style
## Get User Input
denomination = int(input("Please enter the denomination of your bank note in dollars: $"))
person = ""

#if statements:
if denomination == 1:
    person = "George Washington"
elif denomination == 2:
    person = "Thomas Jefferson"
elif denomination == 5:
    person = "Abraham Lincoln"
elif denomination == 10:
    person = "Alexander Hamilton"
elif denomination == 20:
    person = "Andrew Jackson"
elif denomination == 50:
    person = "Ulysses S. Grant"
elif denomination == 100:
    person = "Benjamin Franklin"
else:
    print("That denomination does not exist.")

# print result
print("The individual that appears on your denomination is: {}".format(person))