try:
    number = int(input("Enter a number: "))
    print("the number entered is:", number)
except ValueError as ex:
    print("exeption:", ex)