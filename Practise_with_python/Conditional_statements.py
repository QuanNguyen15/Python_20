age = int(input("\nType an age: "))

is_con_nit = False #default

if age < 10:
    is_con_nit = True
if age < 10:
    print("Child\n")
elif age < 18:
    print("Teen\n")
    if age >= 15 or age <= 17: # if age >= 15 = age  <= 16
        print("Young\n")
else:
    print("Mature\n")