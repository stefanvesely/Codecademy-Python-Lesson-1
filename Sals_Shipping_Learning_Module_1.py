
weight = 41.5
price = 0
#Ground Shipping
if (weight <= 2):
  price = 1.5*weight+20
elif (weight > 2) and (weight <= 6):
  price = 3*weight+20
elif (weight > 6) and (weight <= 10):
  price = 4*weight+20
elif (weight > 10):
  price = 4.75 *weight+20
pricepremium = 125
price = price + pricepremium
print ("Ground Shipping is $"+str(price))

#Drone Shipping

if (weight <= 2):
  dprice = 4.5*weight
elif (weight > 2) and (weight <= 6):
  dprice = 9*weight
elif (weight > 6) and (weight <= 10):
  dprice = 12*weight
elif (weight > 10):
  dprice = 14.25 *weight
dpricepremium = 0
dprice = dprice + dpricepremium
print ("Drone Shipping is $"+str(dprice))

