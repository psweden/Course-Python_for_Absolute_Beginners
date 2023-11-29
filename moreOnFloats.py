ex3 = 1.23 + 2.80
print(round(ex3, 2))

ex2 = (123 + 280) / 100
print(ex2)

# Purchase task
penne = 16.98
arrabiata = 6.98
organicGarlic = 16.78
bottle = 15.36
baguettes = 3.00
meatballs = 4.39
ex1 = penne + arrabiata + organicGarlic + bottle + baguettes + meatballs
print(round(ex1, 2))

# Variables holding the prices of the six items:

pasta = 16.68  # penne 16 oz, pack of 12
sauce = 6.98  # Arrabiata sauce 24oz
garlic = 16.78  # 20 pack garlic clove
seasoning = 15.26  # Italian Seasoning
bread = 3.00  # Baguette twin pack
meatballs = 4.39  # 12 oz bag of meatballs
# A subtotal is the sum of all prices before any sales taxes or discounts are added.

# round() was used to round the subtotal to 2 decimal places since the sum of any amount of numbers that all have 2
# numbers after the decimal will always have 2 numbers after its decimal point.
subtotal = round((pasta + sauce + garlic + seasoning + bread + meatballs), 2)
print(subtotal)

# Variables holding the prices of the six items:

# All of the variables were multiplied by 100 to make them into integers so that there would be no approximation errors
# when they were added together.

pasta = 16.68 * 100  # penne 16 oz, pack of 12
sauce = 6.98 * 100  # Arrabiata sauce 24oz
garlic = 16.78 * 100  # 20 pack garlic clove
seasoning = 15.26 * 100  # Italian Seasoning
bread = 3.00 * 100  # Baguette twin pack
meatballs = 4.39 * 100  # 12 oz bag of meatballs
# subtotal is the sum of all prices before any sales taxes or discounts are added
subtotal = (pasta + sauce + garlic + seasoning + bread + meatballs) / 100
print(subtotal)