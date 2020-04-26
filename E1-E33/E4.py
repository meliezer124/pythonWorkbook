## Area of a Field

# Read size of field
length = float(input("Enter the length of the field in feet:"))
width = float(input("Enter the width of the field in feet:"))

# Calculate area of field
area_in_ft = width * length

# Conversion to acres
area_in_acres = area_in_ft/43560

#Print result
print("Your field is {} acres!".format(area_in_acres))