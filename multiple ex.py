try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print ("result:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except SyntaxError:
    print("Invalid input format. Please enter two numbers separated by a comma.")
except:
    print("wrong input.")
else:
    print(" no exeptions")
finally:
    print("this will execute no matter what")