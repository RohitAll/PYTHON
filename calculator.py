def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if (number2 == 0):
        return "Not Division by zero"
    else:
        return number1 / number2

print('''
1. Addition(+)
2. subtraction(-)
3. multiply(*)
4. Division(/)
''')

select = int(input("Enter Your Operation 1,2,3,4): "))

number1 = int(input("Enter Your First number: "))
number2 = int(input("Enter Your Second number: "))

if (select == 1):
    print(number1, "+", number2 ,"=", addition(number1, number2))
elif (select == 2):
    print(number1, "-", number2 ,"=", subtraction(number1, number2))
elif (select == 3):
    print(number1, "*", number2 ,"=", multiplication(number1, number2))
elif (select == 4):
    print(number1, "/", number2 ,"=", division(number1, number2))
else:
    print("Wrong Select")