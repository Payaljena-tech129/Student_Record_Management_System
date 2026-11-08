
from file_handler import save_students


# Add Student
def add_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    try:
        marks = float(input("Enter Marks: "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid marks.")
        return

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# View Students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


# Search Student
def search_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found:")
            print(student)
            return

    print("Student not found.")


# Update Student
def update_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            name = input("Enter new name (blank to keep): ")
            course = input("Enter new course (blank to keep): ")
            marks_input = input("Enter new marks (blank to keep): ")

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if marks_input:
                try:
                    marks = float(marks_input)

                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return

                    student["marks"] = marks

                except ValueError:
                    print("Invalid marks.")
                    return

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete Student
def delete_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found.")
