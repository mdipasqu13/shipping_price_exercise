weight = 41.5

#Ground Shipping
if weight <= 2:
  ground_shipping = weight * 1.50 + 20
elif weight <= 6:
  ground_shipping = weight * 3.00 + 20
elif weight <= 10:
  ground_shipping = weight * 4.00 + 20
else:
  ground_shipping = weight * 4.75 + 20

print("Ground Shipping Price", ground_shipping)

#Premium Shipping
premium_shipping = 125.00

print("Ground Shipping Premium Price", premium_shipping)

#Drone Shipping
if weight <= 2:
  drone_shipping = weight * 4.50
elif weight <= 6:
  drone_shipping = weight * 9.00
elif weight <= 10:
  drone_shipping = weight * 12.00
else:
  drone_shipping = weight * 14.25

print("Drone Shipping Price", drone_shipping)





