# This is a Simple Calculator project created in a new branch
print("Simple Calculator")

n1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

if op == "+":
    print(f"--- Result: {n1 + n2} ---")
elif op == "-":
    print(f"--- Result: {n1 - n2} ---")
elif op == "*":
    print(f"--- Result: {n1 * n2} ---")
elif op == "/":
    if n2 != 0:
        print(f"--- Result: {n1 / n2} ---")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


    