ex_1 = 'This is a string.'
ex_2 = "This is also a string."
ex_3 = "" # Tom sträng

# Indexnummer --> Som i java --> Substring --> [0123456]
ex_8 = "orange"
print(ex_8[2])
print("apple" [4])
# Skriver ut tecknet plats '2' i orange = a te.x

# String slicing --> Som i java --> Substring
ex_10 = "apricots"
print(ex_10 [:3])  # utskrift = 'apr'
print(ex_10 [2:5]) # utskrift = 'ric'
print(ex_10 [4:])  # utskrift = 'cots'

# concatenation --> Sammanfoga strings
print("pecan" + " " + "pie")

concatenated = "R2" + "_" + "D2"
print(concatenated)      # Utskrift = R2_D2
print(concatenated[3])   # Utskrift = D --> skriver ut alla tecken efter index 3
print(concatenated[1:4]) # Utskrift = 2_D --> skriver ut alla index från index 1 till index 3

unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)        # Utskrift --> t gump
print(unchanged)     # Utskrift --> forrest gump
print(unchanged[10]) # Utskrift --> p
print(unchanged)     # Utskrift --> forrest gump

# String Exercises
ex_11 = "Just do it!"
print(ex_11[10])
print(ex_11[5:7])
print(ex_11[8:11])
print(ex_11[0:4])
ex_slice = "don't" + " " + ex_11[5:11]
print(ex_slice)
