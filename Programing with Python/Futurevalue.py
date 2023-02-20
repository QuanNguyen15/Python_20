def Futurevalue():
    principal = float(input("The amount of money being invested: "))
    apr = float(input("The annual percentage rate: "))
    for i in range (0,10):
        principal = principal*(1+apr)
    print("Total: ", principal)
Futurevalue()
    

