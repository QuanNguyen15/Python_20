import math


def ptbh():
    print("This program finds the real solutions to a quadratic")
    print()

    a = eval(input("Please enter the coefficients a: "))
    b = eval(input("Please enter the coefficients b: "))
    c = eval(input("Please enter the coefficients c: "))
    discRoot = math.sqrt(b * b - 4 * a * c)

    if discRoot < 0:
        print("The coefficients is not the real solutions")
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print("\nThe solutions are:", root1, root2)


ptbh()


def factorials():
    a = eval(input("\nEnter whole number: "))
    fact = 1

    for i in range(a, 1, -1):
        fact = fact * i
    print("The factorial of ", a, "is ", fact)


factorials()


