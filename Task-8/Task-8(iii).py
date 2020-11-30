try:
    a = magnoolia
except NameError:
    print("No name is defined")
try:
    b = 1/0
except ArithmeticError:
    print("Division by zero")
