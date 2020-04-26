def roomSize():
    width = float(input("What is the width of this room in meters?"))
    length = float(input("What is the length of this room in meters?"))
    area = width * length
    print("The area of this room is {} meters squared.".format(area))

roomSize()

### Book Solution -- doesn't use function! ###
# Read input values from user
# length = float(input("Enter the length of the room in feet:"))
# width = float(input("Enter the width of the room in feet:"))

# Computer area of the room
# area = length * width

# Display Result
# print("The area of the room is " , area, " square feet")
