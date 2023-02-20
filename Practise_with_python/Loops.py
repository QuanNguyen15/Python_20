# # print("\nLoop in loop 1: ")
# # for i in range (0,2):
# #     print(i)
# #     for a in range (3,5):
# #         print(a)

# # print("\nLoop in loop 2: ")
# # for i in range (0,2):
# #     for a in range (3,5):
# #         print(a)
# #     print(i)

# # print("\nLoop in loop 3: ")
# # for i in range (0,2):
# #     for a in range (3,5):
# #         print(a)
# #         print(i)        


# # s_denominator = 0 

# # for i in range(100):
# #     if i == 1:
# #         continue

# #     if i % 2 == 0:
# #         continue

# #     s_denominator += 1/i 

# # s = 1/s_denominator
# # s = round(s,2)
# # print("S = " + str(s))

# a = int(input("Enter number: "))
# while a > 0:
#     print("a = ",a)
#     a -=1

# print("---")
# b = str(input("Enter your string: "))
# idx = 0
# length = len(b)

# while idx < length:
#     print(idx, "is", b[idx])
#     idx +=1

# print("---")

# i = int(input("Enter number: "))
# while i < 10:
#     i +=1
#     if i == 5:
#         continue
#     print(i)
# print("\n---\n")

# i = int(input("Enter number: "))
# while True:
#     i +=1
#     if i == 5:

import math


def main():
    print("This program finds the real solutions to a quadratic")
    print()
    a = float(input("Please enter the coefficients a: "))
    b = float(input("Please enter the coefficients b: "))
    c = float(input("Please enter the coefficients c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    print()
    print("The solutions are:", root1, root2)

main()
