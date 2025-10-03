for x in range(int(input("Enter a number: "))):
    if x % 20 ==0:
        print("ice cream")
    elif x % 15 ==0:
        print("chocolate ice cream")
    elif x % 5 ==0:
        print("vanilla ice cream")
    elif x % 3 ==0:
        print("mint chocolate ice cream")
    else:
        print(x)