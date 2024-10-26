# Trying to concatenate a string and an integer, which causes a TypeError
try:
    result = "Hello, " + 12.3  # Concatenating a string and an integer
    print(result)
except TypeError:
    print("You can't concatenate a string and an integer directly!")


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("That's not a valid number!")
# except TypeError:
#     print("That's not a valid TYPE!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
