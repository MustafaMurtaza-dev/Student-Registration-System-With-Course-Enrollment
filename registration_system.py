import os

STUDENT_FILE = "students.txt"
COURSE_FILE = "courses.txt"
ENROLLMENT_FILE = "enrollments.txt"

students = {}
courses = {}
enrollments = []

class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name

    def show_details(self):
        print(f"  Student ID: {self.id}, Name: {self.name}")

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def show_details(self):
        print(f"  Course ID: {self.course_id}, Name: {self.course_name}")

class Enrollment:
    def enroll_student(self, student_id, course_id):
        if student_id not in students:
            print(f"[Error] Student with ID {student_id} not found.")
            return

        if course_id not in courses:
            print(f"[Error] Course with ID {course_id} not found.")
            return

        if (student_id, course_id) in enrollments:
            print(f"[Info] Student {students[student_id].name} is already enrolled in {courses[course_id].course_name}.")
            return

        enrollments.append((student_id, course_id))
        save_enrollments()
        print(f"[Success] Student {students[student_id].name} enrolled in {courses[course_id].course_name}.")

    def show_student_courses(self, student_id):
        if student_id not in students:
            print(f"[Error] Student with ID {student_id} not found.")
            return

        print(f"\n--- Courses for {students[student_id].name} (ID: {student_id}) ---")
        student_enrollments = []
        for sid, cid in enrollments:
            if sid == student_id:
                student_enrollments.append(cid)

        if not student_enrollments:
            print("  This student is not enrolled in any courses.")
        else:
            for course_id in student_enrollments:
                course = courses.get(course_id)
                if course:
                    course.show_details()
        print("-" * 40)

def load_students():
    if not os.path.exists(STUDENT_FILE):
        return
    with open(STUDENT_FILE, 'r') as f:
        for line in f:
            student_id, name = line.strip().split(',')
            students[student_id] = Student(student_id, name)

def save_students():
    with open(STUDENT_FILE, 'w') as f:
        for student in students.values():
            f.write(f"{student.id},{student.name}\n")

def load_courses():
    if not os.path.exists(COURSE_FILE):
        return
    with open(COURSE_FILE, 'r') as f:
        for line in f:
            course_id, course_name = line.strip().split(',')
            courses[course_id] = Course(course_id, course_name)

def save_courses():
    with open(COURSE_FILE, 'w') as f:
        for course in courses.values():
            f.write(f"{course.course_id},{course.course_name}\n")

def load_enrollments():
    if not os.path.exists(ENROLLMENT_FILE):
        return
    with open(ENROLLMENT_FILE, 'r') as f:
        for line in f:
            student_id, course_id = line.strip().split(',')
            enrollments.append((student_id, course_id))

def save_enrollments():
    with open(ENROLLMENT_FILE, 'w') as f:
        for student_id, course_id in enrollments:
            f.write(f"{student_id},{course_id}\n")

def main():
    load_students()
    load_courses()
    load_enrollments()

    enrollment_manager = Enrollment()

    while True:
        print("\n===== Student Course Registration System =====")
        print("1. Register New Student")
        print("2. Show All Courses")
        print("3. Enroll Student in Course")
        print("4. Show Student Enrollments")
        print("5. Exit")
        print("=" * 42)

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                student_id = input("Enter new Student ID: ")
                if student_id in students:
                    print(f"[Error] Student with ID {student_id} already exists.")
                    continue
                
                name = input("Enter Student Name: ")
                if not name:
                    print("[Error] Name cannot be empty.")
                    continue

                students[student_id] = Student(student_id, name)
                save_students()
                print(f"[Success] Student '{name}' registered with ID {student_id}.")

            except Exception as e:
                print(f"[Error] An unexpected error occurred: {e}")

        elif choice == '2':
            print("\n--- Available Courses ---")
            if not courses:
                print("  No courses available.")
            else:
                for course in courses.values():
                    course.show_details()
            print("-" * 25)

        elif choice == '3':
            print("\n--- Enroll in a Course ---")
            student_id = input("Enter Student ID to enroll: ")
            course_id = input("Enter Course ID to enroll in: ")
            enrollment_manager.enroll_student(student_id, course_id)

        elif choice == '4':
            print("\n--- View Student Enrollments ---")
            student_id = input("Enter Student ID: ")
            enrollment_manager.show_student_courses(student_id)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("[Error] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
