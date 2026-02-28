print("Simple Calculator")

n1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

if op == "+":
    print("Answer: ",n1+n2)
elif op == "-":
    print("Answer: ",n1-n2)
elif op == "*":
    print("Answer: ",n1*n2)
elif op == "/":
    if n2 != 0:
        print("Answer: ",n1/n2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


    