def main():
    student_A_name = "Quan"
    student_B_name = "Nguyen"
    print_number(2, 10, 3)
    print_student_A(student_A_name)
    print_student_B(student_B_name)


def print_number(min_number, max_number, distance):
    for i in range(min_number, max_number, distance):
        print(i, end=' ')
    print("\n")


def print_student_A(name):  # chuyền parameter vào hàm print_student_A với Parameter name = student_A_name
    print("Student A")
    print("Name: " + name)
    print("Toan: 9")
    print("Van: 6\n")


def print_student_B(name):
    print("Student B")
    print("Name: " + name)
    print("Toan: 8")
    print("Van: 7")


# student_A_name = "Quan" global variable không nên sử dụng hàm globla variable 


main()
