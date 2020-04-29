## Widgets and Gizmos ##

# Define weights
widget_weight = 75
gizmo_weight = 112

# Number of each in order from use
widget_order = float(input("How many widgets do you want?"))
gizmo_order = float(input("How many gizmos do you want?"))

#compute and print total weight
total_weight = (widget_order * widget_weight) + (gizmo_order * gizmo_weight)
print("The total weight of your order is {}".format(total_weight))
