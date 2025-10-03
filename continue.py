icecream = int(input("Enter the number of ice cream you want: "))
while icecream > 0:
    icecream = icecream -1
    if icecream == 5 or icecream == 34:
        continue
    print('\ncurrent variable value :', icecream)
print("We are out of ice cream")