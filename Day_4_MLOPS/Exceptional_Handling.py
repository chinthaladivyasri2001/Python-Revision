# Handling division by zero error
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution complete.")

# Test cases
divide(10, 2)
divide(10, 0)

#Raising a custom exception
def validate_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    else:
        print("Valid age")

# Test case
try:
    validate_age(15)
except ValueError as e:
    print(e)
