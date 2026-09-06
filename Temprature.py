temp=float(input("Enter Temprature:"))
unit=(input("Is this Temprature in Celcius or Fahrenheit(C or F): "))
if unit=="C":
    temp=(temp*(9/5))+32
    print(f"{round(temp,2)}°F is in Fahrenheit")
elif unit=="F":
    temp=(temp-32)*5/9
    print(f"{round(temp,2)}°C in Celcius")
