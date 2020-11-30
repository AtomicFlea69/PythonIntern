print("Choose a operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Select a choice:")

    if choice in('1','2','3','4'):
        num1 = int(input("Enter a number:"))
        num2 = int(input("Enter a number:"))

        if choice == '1':
            print(num1 + num2)
        elif choice == '2':
            print(num1 - num2)
        elif choice == '3':
            print(num1 * num2)
        elif choice == '4':
            try:
                num1 / num2
            except ZeroDivisionError:
                print("Division by zero is infinity")
        break
    else:
        print("Enter a valid choice")