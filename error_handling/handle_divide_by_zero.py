try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print(f"Result is: {result}")
finally:
    print("This runs no matter what.")
