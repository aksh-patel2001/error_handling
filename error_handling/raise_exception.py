try:
    age = -1
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)
