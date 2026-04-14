def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q
print("Please select the operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Please enter choice (a/ b/ c/ d): ")
num_one = int(input("Please enter the first number: "))
num_two = int(input("Please enter the second number: "))
if choice == 'a':
    print(num_one, "+", num_two, "=", add(num_one, num_two))
elif choice == 'b':
    print(num_one, "-", num_two, "=", subtract(num_one, num_two))
elif choice == 'c':
    print(num_one, "*", num_two, "=", multiply(num_one, num_two))
elif choice == 'd':
    print(num_one, "/", num_two, "=", divide(num_one, num_two))
else:
    print("This is an invalid input")