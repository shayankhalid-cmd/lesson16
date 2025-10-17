n = int(input("enter the range of numbers form 1"))
odd = [x for x in range(1,n) if x%2!=0  ]
print("list of odd numbers from original:",odd)
fruits = ["strawberry","apple","blueberry","mango","blackberry","tomato"]
fruit =[fruit.capitalize() for fruit in fruits]
print(fruit)