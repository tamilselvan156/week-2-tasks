# Student Grade Management System
print("\n" + "="*50)
print("         Student Grade Calculator")
print("="*50)

students = []      # List to store student names
grades = []        # List to store student marks

# Input number of students with validation
while True:
    try:
        num_students = int(input("Enter the number of students: "))
        if num_students > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter an integer.")

# Input student details
for i in range(num_students):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    # Input marks with validation
    while True:
        try:
            mark = float(input("Enter marks (0-100): "))
            if 0 <= mark <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter numeric marks.")

    students.append(name)
    grades.append(mark)

# Display report
print("\n================ STUDENT REPORT ================")
print("{:<15}{:<10}{:<8}{}".format("Name", "Marks", "Grade", "Comment"))
print("-" * 55)

# Process each student
for i in range(num_students):

    if grades[i] >= 90:
        grade = "A+"
        comment = "Outstanding!"
    elif grades[i] >= 80:
        grade = "A"
        comment = "Excellent!"
    elif grades[i] >= 70:
        grade = "B"
        comment = "Very Good!"
    elif grades[i] >= 60:
        grade = "C"
        comment = "Good."
    elif grades[i] >= 50:
        grade = "D"
        comment = "Needs Improvement."
    else:
        grade = "F"
        comment = "Fail. Work Harder."

    print("{:<15}{:<10}{:<8}{}".format(
        students[i], grades[i], grade, comment))

# Calculate statistics
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

# Display statistics
print("\n============== STATISTICS ==============")
print("Average Marks :", round(average, 2))
print("Highest Marks :", highest)
print("Lowest Marks  :", lowest)
print("\n" + "=" *50)
print("Thanks you for using grade calculator")
print("="*50)
