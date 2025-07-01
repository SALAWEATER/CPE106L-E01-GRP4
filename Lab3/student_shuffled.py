import random
from student import Student

def main():
    # Create several Student objects with different names and scores
    students = [
        Student("Alice", 3),
        Student("Bob", 3),
        Student("Charlie", 3),
        Student("Diana", 3)
    ]

    # Set some scores for each student
    for i, student in enumerate(students):
        for j in range(1, 4):
            student.setScore(j, 70 + i * 5 + j)

    # Shuffle the list
    random.shuffle(students)
    print("Shuffled students:")
    for student in students:
        print(student)
        print()

    # Sort the list (uses __lt__ in Student)
    students.sort()
    print("Sorted students:")
    for student in students:
        print(student)
        print()

if __name__ == "__main__":
    main()