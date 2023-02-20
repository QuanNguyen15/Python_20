def Ex1():
    a = eval(input("Enter number : "))

    n1 = eval("%s" % a)
    n2 = eval("%s%s" % (a, a))
    n3 = eval("%s%s%s" % (a, a, a))
    print(n1 + n2 + n3)


Ex1()
