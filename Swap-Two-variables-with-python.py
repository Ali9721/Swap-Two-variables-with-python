# Define "a" & "b" as variables .
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

# Define "a" & "b" to exchange each others.
a, b = b, a

# Output the result.
print(f"After swapping: a = {a}, b = {b}")
