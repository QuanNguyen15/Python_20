def main():
    student_A_name = "Quan"
    student_A_math_score = 9
    student_A_literatur_score = 8

    student_B_name = "Nguyen"
    student_B_math_score = 8
    student_B_literatur_score = 9

    print_student(student_A_name, student_A_math_score, student_A_literatur_score )
    print_student(student_B_name, student_B_math_score, student_B_literatur_score )

def print_student(name, math_score, literature_score):
    print("Student name: " + name)
    print("Math score: " + str(math_score)) 
    print("Literature score: " + str(literature_score))
    print('\n')


main()
  