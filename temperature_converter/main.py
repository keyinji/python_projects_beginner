

temperature = input("What's the base temperature? ")

try:
    temperature = int(temperature)
except:
    print("Invalid input")
    exit()

base = input("Farenheight or Celsius? ").upper()

if base == "C":
    print("The temperature in Farenheight is", round(temperature * 1.8 + 32, 2), "F")
elif base == "F":
    print("The temperature in Celsius is", round((temperature - 32) / 1.8, 2), "C")
else:
    print("Invalid input")




