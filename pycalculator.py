

operator = input("Enter an operator (+, - ,* , ** /): ")
num1 = int(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if operator == "+" :
    result = (num1 + num2)
    print(result)
    
elif operator =="-" :
    result = (abs(num1 - num2))
    print(result)
    

elif operator == "*" :
    result = num1 * num2
    print(result)
    
elif operator == "**":
    result = num1 ** num2
    print(result)
   

else:
    print("not a valid operator")
    