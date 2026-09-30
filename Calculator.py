def addition(num1, num2):
    result1 = num1 + num2
    return result1


def subtraction(num1, num2):
    result2 = num1 - num2
    return result2


def multiplication(num1, num2):
    result3 = num1 * num2
    return result3


def divide(num1, num2):
    result4 = num1 / num2
    return result4


while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Exit")

    operation = int(input("Enter your operation: "))

    if operation == 5:
        print("Calculator closed")
        break

    if operation < 1 or operation > 5:
        print("Wrong operation! Please try again.")
        continue

    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    if operation == 1:
        print(f"Sum = {addition(num1, num2)}")

    elif operation == 2:
        print(f"Subtraction = {subtraction(num1, num2)}")

    elif operation == 3:
        print(f"Multiplication = {multiplication(num1, num2)}")

    elif operation == 4:
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"Divide = {divide(num1, num2)}")