try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be at least 18.")
    print("Access granted.")
except ValueError as ve:
    print("Access denied. You must be at least 18 years old.")