import json
import os
from datetime import datetime

# ANSI colors for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=4)

    def calculate_grade(self, marks):
        avg = sum(marks) / len(marks)

        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        else:
            return 'F'

    def generate_id(self):
        if not self.students:
            return "STU001"

        last_id = self.students[-1]['id']
        number = int(last_id[3:]) + 1
        return f"STU{number:03d}"

    def add_student(self):
        print(f"\n{Colors.BLUE}=== Add New Student ==={Colors.END}")

        name = input("Enter Name: ").strip()

        if not name:
            print(f"{Colors.RED}Name cannot be empty!{Colors.END}")
            return

        try:
            age = int(input("Enter Age: "))

            if age < 5 or age > 100:
                raise ValueError

        except ValueError:
            print(f"{Colors.RED}Invalid Age!{Colors.END}")
            return

        subjects = ["Math", "Science", "English"]
        marks = []

        for subject in subjects:
            try:
                mark = float(
                    input(f"Enter {subject} Marks (0-100): ")
                )

                if mark < 0 or mark > 100:
                    raise ValueError

                marks.append(mark)

            except ValueError:
                print(
                    f"{Colors.RED}Invalid marks for {subject}!{Colors.END}"
                )
                return

        student = {
            "id": self.generate_id(),
            "name": name,
            "age": age,
            "marks": dict(zip(subjects, marks)),
            "average": round(sum(marks) / len(marks), 2),
            "grade": self.calculate_grade(marks),
            "date_added": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        self.students.append(student)
        self.save_data()

        print(
            f"{Colors.GREEN}Student Added Successfully! "
            f"ID: {student['id']} | Grade: {student['grade']}"
            f"{Colors.END}"
        )

    def display_all(self):
        if not self.students:
            print(
                f"{Colors.YELLOW}No student records found!{Colors.END}"
            )
            return

        print(
            f"\n{Colors.BOLD}"
            f"{'ID':<10}{'Name':<20}{'Age':<6}"
            f"{'Average':<10}{'Grade':<8}"
            f"{Colors.END}"
        )

        print("-" * 60)

        for s in self.students:
            print(
                f"{s['id']:<10}"
                f"{s['name']:<20}"
                f"{s['age']:<6}"
                f"{s['average']:<10}"
                f"{s['grade']:<8}"
            )

        class_avg = sum(
            s['average'] for s in self.students
        ) / len(self.students)

        print(
            f"\n{Colors.BLUE}"
            f"Total Students: {len(self.students)}"
            f" | Class Average: {round(class_avg,2)}"
            f"{Colors.END}"
        )

    def search_student(self):
        keyword = input(
            "Enter Student ID or Name: "
        ).strip().lower()

        results = [
            s for s in self.students
            if keyword in s['id'].lower()
            or keyword in s['name'].lower()
        ]

        if not results:
            print(f"{Colors.RED}Student not found!{Colors.END}")
            return

        for s in results:
            print(f"\n{Colors.BOLD}Student Details{Colors.END}")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")

            print("Marks:")
            for subject, mark in s['marks'].items():
                print(f"  {subject}: {mark}")

            print(f"Average: {s['average']}")
            print(f"Grade: {s['grade']}")
            print(f"Date Added: {s['date_added']}")

    def update_student(self):
        student_id = input(
            "Enter Student ID: "
        ).strip().upper()

        student = next(
            (s for s in self.students
             if s['id'] == student_id),
            None
        )

        if not student:
            print(f"{Colors.RED}Student not found!{Colors.END}")
            return

        name = input(
            f"Name [{student['name']}]: "
        ).strip()

        if name:
            student['name'] = name

        age = input(
            f"Age [{student['age']}]: "
        ).strip()

        if age:
            try:
                student['age'] = int(age)
            except ValueError:
                print("Invalid age skipped.")

        for subject in student['marks']:
            value = input(
                f"{subject} [{student['marks'][subject]}]: "
            ).strip()

            if value:
                try:
                    score = float(value)

                    if 0 <= score <= 100:
                        student['marks'][subject] = score

                except ValueError:
                    pass

        marks = list(student['marks'].values())

        student['average'] = round(
            sum(marks) / len(marks), 2
        )

        student['grade'] = self.calculate_grade(marks)

        self.save_data()

        print(
            f"{Colors.GREEN}Student Updated Successfully!"
            f"{Colors.END}"
        )

    def delete_student(self):
        student_id = input(
            "Enter Student ID: "
        ).strip().upper()

        student = next(
            (s for s in self.students
             if s['id'] == student_id),
            None
        )

        if not student:
            print(f"{Colors.RED}Student not found!{Colors.END}")
            return

        confirm = input(
            f"Delete {student['name']}? (y/n): "
        ).lower()

        if confirm == 'y':
            self.students.remove(student)
            self.save_data()

            print(
                f"{Colors.GREEN}Student Deleted Successfully!"
                f"{Colors.END}"
            )

    def filter_by_grade(self):
        grade = input(
            "Enter Grade (A+,A,B,C,D,F): "
        ).upper()

        results = [
            s for s in self.students
            if s['grade'] == grade
        ]

        if not results:
            print(
                f"{Colors.YELLOW}No students found!"
                f"{Colors.END}"
            )
            return

        for s in results:
            print(
                f"{s['id']} - {s['name']} "
                f"({s['average']})"
            )

    def backup_data(self):
        backup_file = (
            f"backup_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        with open(backup_file, 'w') as f:
            json.dump(self.students, f, indent=4)

        print(
            f"{Colors.GREEN}Backup Created: "
            f"{backup_file}{Colors.END}"
        )


def main():
    manager = StudentManager()

    while True:
        print(f"\n{Colors.BOLD}=== Student Management System ==={Colors.END}")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Filter By Grade")
        print("7. Backup Data")
        print("8. Exit")

        choice = input("Enter Choice: ").strip()

        if choice == '1':
            manager.add_student()

        elif choice == '2':
            manager.display_all()

        elif choice == '3':
            manager.search_student()

        elif choice == '4':
            manager.update_student()

        elif choice == '5':
            manager.delete_student()

        elif choice == '6':
            manager.filter_by_grade()

        elif choice == '7':
            manager.backup_data()

        elif choice == '8':
            print(
                f"{Colors.GREEN}Goodbye!{Colors.END}"
            )
            break

        else:
            print(
                f"{Colors.RED}Invalid Choice!{Colors.END}"
            )


if __name__ == "__main__":
    main()