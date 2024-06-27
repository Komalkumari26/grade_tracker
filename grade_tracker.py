class StudentGradeManager:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count != 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A', 4.0
        elif average >= 80:
            return 'B', 3.0
        elif average >= 70:
            return 'C', 2.0
        elif average >= 60:
            return 'D', 1.0
        else:
            return 'F', 0.0

    def display_grades(self):
        print("\nGrade Summary:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

        average = self.calculate_average()
        letter_grade, gpa = self.get_letter_grade(average)

        print(f"\nAverage Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")

def main():
    manager = StudentGradeManager()

    print("Enter grades for subjects or assignments. Type 'done' when finished.")
    while True:
        subject = input("Enter the subject or assignment name: ")
        if subject.lower() == 'done':
            break

        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            manager.add_grade(subject, grade)
        except ValueError:
            print("Invalid input! Please enter a numeric value for the grade.")

    if manager.grades:
        manager.display_grades()
    else:
        print("No grades entered.")

# Run the grade management function
if __name__ == "__main__":
    main()
