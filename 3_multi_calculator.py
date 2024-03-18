# Valeriia Pasichna
# G12460782 

Sum = 0

# 1. input

x1= input("Type x1: ")
x2= input("Type x2: ")
op = input ("Enter operator: ")

# 2. Process
if op == "+":
    sum = int(x1) + int (x2)
elif op == "-":
    sum = int(x1) - int(x2)
elif op == "*":
    sum = int(x1) * int(x2)
elif op == "/":
    sum = int(x1) / int(x2)

# 3. Output

print(f"Sum: {sum}")