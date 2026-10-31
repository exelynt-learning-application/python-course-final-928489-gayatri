# Student Grade Calculator

# Take student name as input
student_name = input("Enter student name: ")

# Take marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Validate marks
if (0 <= subject1 <= 100 and
    0 <= subject2 <= 100 and
    0 <= subject3 <= 100):

    # Calculate total and average
    total = subject1 + subject2 + subject3
    average = total / 3

    # Calculate grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Display student result
    print("\n----- Student Result -----")
    print("Student Name:", student_name)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

else:
    print("Invalid marks! Please enter marks between 0 and 100.")
