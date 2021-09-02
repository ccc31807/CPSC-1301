#!python
# Name: Recurethods.py
# Author: Charles Carter
# Date; May 22, 2021
# Purpose: does grading by recursive methods

def hello():
    print("Hello from 'RecurMethods.py'")
    print()

def sum_ten(start, end, accum):
    #print("Calling sum_ten(", start, end, accum, ")")
    if start >= end:
        return accum
    else:
        start += 1
        print(start, "Enter the next grade of", end, "grades: ")
        grade = int(input())
        return sum_ten(start, end, accum + grade)

def sum_any(counter, accum):
    #print("Calling sum_any(", counter, accum, ")")
    print("Enter the next grade, -1 to exit: ")
    grade = int(input())
    if grade < 0:
        return (counter, accum)
    else:
        return sum_any(counter + 1, accum + grade)

def letter_grade(num_grade):
    if num_grade >= 90.0:
        return "A"
    elif num_grade >= 80.0:
        return "B"
    elif num_grade >= 70.0:
        return "C"
    elif num_grade >= 60.0:
        return "D"
    else:
        return "F"

#main function executes the defined functions
if __name__ ==  '__main__':
    hello()
    print()

    print("calling sum_ten() and calculating the final letter grade")
    start = 0
    end = 10
    accum = 0
    total_grades = sum_ten(start, end, accum)
    average_grade = float(total_grades) / float(end)
    let_grade = letter_grade(average_grade)
    print("Total of grades is", total_grades)
    print("Average of grades is", average_grade)
    print("Letter grade is", let_grade)
    print()

    '''
    #student version
    print("calling sum_any() and calculating the final letter grade")
    #initialize the follow variables and write the method sum_any()
    start = None
    end = None
    accum = None
    total_grades = sum_any(start, end, accum)
    average_grade = total_grades / end
    let_grade = letter_grade(average_grade)
    print("Total of grades is", total_grades)
    print("Average of grades is", average_grade)
    print("Letter grade is", let_grade)
    print()
    '''

    #instructor version
    print("calculating the final letter grade for a user defined limit")
    start = 0
    print("How many grades do you have: ")
    end = int(input())
    accum = 0
    total_grades = sum_ten(start, end, accum)
    average_grade = total_grades / end
    let_grade = letter_grade(average_grade)
    print("Total of grades is", total_grades)
    print("Average of grades is", average_grade)
    print("Letter grade is", let_grade)
    print()

    print("calculating the final grade for an arbitrary number of grades, no pre-specified limit")
    accum = 0
    counter = 0
    (counter, total_grades) = sum_any(counter, accum)
    average_grade = total_grades / counter
    let_grade = letter_grade(average_grade)
    print("Total of grades is", total_grades)
    print("Average of grades is", average_grade)
    print("Letter grade is", let_grade)
    print()


    


