try:
    num = 0
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution complete.")
    a = 20
    b = 20
    print(a == b)
