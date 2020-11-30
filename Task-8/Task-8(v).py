try:
    a = int(input("Enter a value:"))
    b = a / 0
except ZeroDivisionError:
    print("Not an error")