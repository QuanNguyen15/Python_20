import datetime

def ask_yes_no(promt):
    while True:
        answer = input(promt)
        if (answer == "yes"):
            return True
        elif (answer == "no"):
            return False
        else:
            continue


def calc_age(year_born):
    now = datetime.datetime.now()
    CURRENT_YEAR = now.year  # Constant variable
    return CURRENT_YEAR - year_born


def covert_meter_to_feet(meter):
    METER_TO_FEET = 3.281
    feet = meter * METER_TO_FEET
    feet = round(feet, 1)  # overwrite
    return feet


def print_height_infor(height_feet, is_male):  # check height
    if is_male:
        if height_feet > 6.5:
            print("Your are", end=' ')

            for i in range(5):
                print("very", end=' ')

            print("tall as a man\n")
        elif height_feet > 6.0:
            print("Your are tall as a man")
        else:
            print("Your are short as a man\n")

    else:
        if height_feet > 5.7:
            print("Your are tall as a girl\n")
        elif height_feet < 5.0:
            print("Your are", end=' ')
            i = 0
            while i < 5:
                print("very", end=' ')
                i += 1

            print("short as a girl")

        else:
            print("Your are short as a girl")


def print_person_infor(firstname, lastname, age, height_feet, is_vietnamese, is_male):
    now = datetime.datetime.now()
    CURRENT_YEAR = now.year
    print("\nYour name is " + firstname + " " + lastname)
    print("{2} is {0} years old in {1}".format(age, CURRENT_YEAR, firstname))  # string format
    print("Your height in meter is " + str(height_feet) + " feet tall")
    # chek national
    if is_vietnamese:
        print("You are from Vietnam")
    else:
        print("You are not from Vietnam")
    print_height_infor(height_feet, is_male)


def ask_person_infor():
    firstname = str(input("\nYour firstname: "))
    lastname = str(input("Your lastname: "))
    year_born = int(input("When you were born: "))
    height_meter = float(input("Your height (meter): "))
    is_male = ask_yes_no("Are you male (yes/no): ")
    is_vietnamese = ask_yes_no("Are you vietnamese (yes/no): ")
    return firstname, lastname, year_born, height_meter, is_male, is_vietnamese


def main():
    firstname, lastname, year_born, height_meter, is_male, is_vietnamese = ask_person_infor()
    age = calc_age(year_born)
    height_feet = covert_meter_to_feet(height_meter)
    print_person_infor(firstname, lastname, age, height_feet, is_vietnamese, is_male)


main()
