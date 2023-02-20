# def CtoF():
#     Celsius = eval(input("Enter Celsius: "))
#     Fahrenheit = (Celsius * 1.8) + 32
#     Fahrenheit = float(Fahrenheit)
#     Fahrenheit = round(Fahrenheit, 1)
#     print(str(Celsius) + " Celsius = " + str(Fahrenheit) + " Fahrenheit")
# CtoF()
#
#
# def FtoC():
#     print("---")
#     Fahrenheit = eval(input("Enter Fahrenheit: "))
#     Celsius = (Fahrenheit - 32) * 0.55
#     Celsius = float(Celsius)
#     Celsius = round(Celsius, 1)
#     print(str(Fahrenheit) + " Fahrenheit = " + str(Celsius) + " Celsius")
#
#
# FtoC()


def ask_infor():
    Celsius = float(input("\nEnter Celsius: "))
    Fahrenheit = float(input("Enter Fahrenheit: "))
    print('---')
    return Celsius, Fahrenheit


def calc(Celsius, Fahrenheit):
    Fahrenheit1 = (Celsius * 1.8) + 32
    Celsius1 = (Fahrenheit - 32) * 0.55
    Celsius1 = round(Celsius1, 2)
    Fahrenheit1 = round(Fahrenheit1, 2)
    return Celsius1, Fahrenheit1


def print_degree(Celsius, Fahrenheit, Celsius1, Fahrenheit1):
    print(str(Celsius) + ' Celsius = ' + str(Fahrenheit1) + ' Fahrenheit')
    print(str(Fahrenheit) + ' Fahrenheit = ' + str(Celsius1) + ' Celsius')


def main():
    Celsius, Fahrenheit = ask_infor()
    Celsius1, Fahrenheit1 = calc(Celsius, Fahrenheit)
    print_degree(Celsius, Fahrenheit, Celsius1, Fahrenheit1)


main()



