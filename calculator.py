#Basic  Calculator  programme

#Get user input
num1 = float( input("enter the first number" ))
num2 =float(input("enter the second number"))
operation= input("enter an operation (+,-,/,*) :")

#Perform The Operations 
if opearation == '+' :
    result=num1+num2
    print( f"{num1} +{num2} ={result}")
elif operation == '-' : 
    result=num1-num2
    print( f"{num1}-{num2}={result} ") 
elif operation == "*" :
    result=num1 * num2 
    print ( f"{num1} *{num2} = {result}") 
elif operation == "/" :
    if num2 == 0:
        print("Error! Division by zero is not allowed .")
    else:
        result = num1/num2
        print(f"{num1}/{num2} ={result}")
else:
    print("Invalid operation! Please enter +, -, *, or/.")        

