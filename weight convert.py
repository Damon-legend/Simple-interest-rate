# weight converter

weight = float(input("Enter the value of the weight: "))
unit = input("is the weight in kilograms or pounds(kg/lb): ")

if unit == "kg" :
    unit = weight * 2.205
    print(f"the weight is {unit} lb")
elif unit == "lb" : 
    unit = weight / 2.205
    print(f"the weight is {unit}kg")
else:
    print("the unit of the weight is invalid")
    