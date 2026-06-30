def calculate_Average(a, b, c):
    sum_of_section_A = sum(a)/len(a)
    sum_of_section_B = sum(b)/len(b)
    sum_of_section_C = sum(c)/len(c)

    print("Average Marks:")
    print("Section A:", sum_of_section_A)
    print("Section B:", sum_of_section_B)
    print("Section C:", sum_of_section_C)

    if sum_of_section_A >= sum_of_section_B and sum_of_section_A >= sum_of_section_C:
        winner = "A"
        averageMark = sum_of_section_A
    elif sum_of_section_B >= sum_of_section_A and sum_of_section_B >= sum_of_section_C:
        winner = "B"
        averageMark = sum_of_section_B
    else:
        winner = "C"
        averageMark = sum_of_section_C

    print("Winner Section:", winner)
    print("Highest Average mark by section:", averageMark)



section_A = [89, 85, 75, 65, 50]
section_B = [90, 75, 65, 70, 95]
section_C = [98, 50, 65, 85, 90]

calculate_Average(section_A, section_B, section_C)




""" def calculate_Average():
    input_A= input("Please enter your all subject marks for Section A follwed by ',':")
    input_B= input("Please enter your all subject marks for Section B follwed by ','':")
    input_C= input("Please enter your all subject marks for Section C follwed by ',':")

    splited_A = input_A.split(",")
    splited_B = input_B.split(",")
    splited_C = input_C.split(",")

    print(splited_A, splited_B, splited_C)
    a = int(splited_A)
    b = int(splited_B)
    c = int(splited_C)

    print(a, b, c)
    sum_of_section_A = sum(a)/len(a)
    sum_of_section_B = sum(b)/len(b)
    sum_of_section_C = sum(c)/len(c)

    print("Average Marks:")
    print("Section A:", sum_of_section_A)
    print("Section B:", sum_of_section_B)
    print("Section C:", sum_of_section_C)

    if sum_of_section_A >= sum_of_section_B and sum_of_section_A >= sum_of_section_C:
        winner = "A"
        averageMark = sum_of_section_A
    elif sum_of_section_B >= sum_of_section_A and sum_of_section_B >= sum_of_section_C:
        winner = "B"
        averageMark = sum_of_section_B
    else:
        winner = "C"
        averageMark = sum_of_section_C

    print("Winner Section:", winner)
    print("Highest Average mark by section:", averageMark)

calculate_Average() """