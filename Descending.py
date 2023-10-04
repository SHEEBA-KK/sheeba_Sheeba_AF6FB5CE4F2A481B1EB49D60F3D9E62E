class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of student objects based on CGPA in descending order
    student_list.sort(key=lambda student: student.cgpa, reverse=True)

# Test the function with a list of student objects
if __name__ == "__main__":
    students = [
        Student("Alice", "101", 3.8),
        Student("Bob", "102", 3.5),
        Student("Charlie", "103", 4.0),
        Student("David", "104", 3.9),
    ]

    print("Original List:")
    for student in students:
        print(f"{student.name}, {student.roll_number}, CGPA: {student.cgpa}")

    sort_students(students)

    print("\nSorted List (by CGPA in descending order):")
    for student in students:
        print(f"{student.name}, {student.roll_number}, CGPA: {student.cgpa}")
