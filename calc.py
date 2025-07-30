import sys

# Step 1: Check argument count
if len(sys.argv) != 4:
    print("Usage: python calc.py <num1> <operator> <num2>")
    sys.exit()

# Step 2: Parse inputs
try:
    num1 = float(sys.argv[1])
    operator = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print("Error: Please enter valid numbers.")
    sys.exit()

# Step 3: Perform arithmetic operation
if operator == '+':
    print(f"Result: {num1 + num2}")
elif operator == '-':
    print(f"Result: {num1 - num2}")
elif operator == '*':
    print(f"Result: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by zero")
else:
    print("Unsupported operator. Use +, -, *, or /")
