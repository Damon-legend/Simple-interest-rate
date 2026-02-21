# temperature converter

unit = input(" is the unit in celcius or fahrenheit (C/F): ")
temp = float(input("Enter the value of the temperature: "))

if unit == "C" :
    temp = (temp * 9/5) + 32
    print(f"the temperature is {temp} °F")
elif temp == "F" :
     temp = (temp -32) * 5/9
     print(f"the temperature is {temp} °C")
else: 
    print("the unit of temperature is invalid")
