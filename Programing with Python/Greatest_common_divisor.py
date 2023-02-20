# Solution1
import math

a = eval(input("Enter number a: "))
b = eval(input("Enter number b: "))

print("The gcd of", a, "and", b, "is: ", end='')
print(math.gcd(a, b))
print('---')

# Solution2
def G_C_D(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y

x = eval(input("Enter x: "))
y = eval(input("Enter y: "))
print("GCD of", x, "and", y, "is", G_C_D(x, y))
