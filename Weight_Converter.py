weight=float(input("Enter an weight:"))
unit=input("kilograms or Pounds (K or L):")

if unit=="K":
    weight=weight*2.205
    print(f"{weight} in Pounds(L)")
elif unit=="L":
    weight=weight/2.205
    print(f"{weight} in Killograms(K)")
else:
    print(f"{unit} was  Invalid  ")