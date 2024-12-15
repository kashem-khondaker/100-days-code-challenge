class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}  # Dictionary to store subject and score

    def add_marks(self, subject, score):
        self.marks[subject] = score


class StudentManager:
    def __init__(self):
        self.students = []  # List to store all Student instances

    def add_student(self, student):
        """Add a new student to the list."""
        self.students.append(student)
        print(f"Student {student.name} added successfully!\n")

    def display_students(self):
        """Display all students and their marks."""
        if not self.students:
            print("No students to display!\n")
            return

        print("\nList of Students:")
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}")
            if student.marks:
                print("Marks:")
                for subject, score in student.marks.items():
                    print(f"  {subject}: {score}")
            else:
                print("  No marks available.")
            print()

    def search_student_by_roll(self, roll):
        """Search for a student using their roll number."""
        for student in self.students:
            if student.roll_number == roll:
                print(f"Student Found: {student.name}\n")
                return student
        print("Student not found!\n")
        return None

    def add_or_update_marks(self, roll, subject, score):
        """Find a student and add or update their marks."""
        student = self.search_student_by_roll(roll)
        if student:
            student.add_marks(subject, score)
            print(f"Marks updated for {subject}: {score}\n")

    def calculate_average_marks(self):
        """Calculate and display average marks for all students."""
        total_sum = 0
        total_subjects = 0

        for student in self.students:
            total_subjects += len(student.marks)
            total_sum += sum(student.marks.values())

        if total_subjects == 0:
            print("No marks available to calculate average.\n")
            return

        avg = total_sum / total_subjects
        print(f"Total Marks: {total_sum}\nSubjects: {total_subjects}\nAverage: {avg:.2f}\n")


# Main Program
manager = StudentManager()

while True:
    print("\n\n1. Add a new student")
    print("2. View all students")
    print("3. Search for a student by roll number")
    print("4. Add/update marks for a student")
    print("5. Calculate average marks")
    print("6. Exit")

    try:
        choice = int(input("Please enter your choice (1-6): "))

        if choice == 1:
            name = input("Enter student's name: ")
            roll = input("Enter roll number: ")
            student = Student(name, roll)
            manager.add_student(student)

        elif choice == 2:
            manager.display_students()

        elif choice == 3:
            roll = input("Enter roll number to search: ")
            manager.search_student_by_roll(roll)

        elif choice == 4:
            roll = input("Enter roll number: ")
            subject = input("Enter subject name: ")
            score = int(input("Enter marks: "))
            manager.add_or_update_marks(roll, subject, score)

        elif choice == 5:
            manager.calculate_average_marks()

        elif choice == 6:
            print("The End ...")
            break

        else:
            print("Invalid input, please input a number between 1 and 6.")

    except ValueError:
        print("Invalid input! Please enter a number.")
