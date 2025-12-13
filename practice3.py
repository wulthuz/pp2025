import numpy as np

class Student:
    def __init__(self, _id, _name, _dob):
        self.id = _id
        self.name = _name
        self.dob = _dob

    def getStudentName(self):
        return self.name

    def printNameAndId(self):
        print(self.id.ljust(15), self.name.ljust(20), end="")

    def printInfo(self):
        print(self.id.ljust(15), self.name.ljust(20), self.dob)


class Course:
    def __init__(self, _id, _name, studentList):
        self.id = _id
        self.name = _name
        self.studentList = studentList
        self.markList = [None] * len(studentList)

    def printCourse(self):
        print(self.id.ljust(15), self.name)

    def printMark(self, idx):
        print(self.markList[idx])


students = []
courses = []

# Input number of students
numOfStudents = int(input("How many students are there in a class ? "))

# Input student information
for i in range(numOfStudents):
    print(f"Student {i+1}'s informations: ")
    _id = input("Id: ")
    _name = input("Name: ")
    _dob = input("Dob (format: dd/mm/yy): ")
    students.append(Student(_id, _name, _dob))

# Input number of courses
numOfCourses = int(input("How many courses are there ? "))

# Input course information
for j in range(numOfCourses):
    print(f"Course {j+1}'s informations: ")
    _id = input("Id: ")
    _name = input("Name: ")
    courses.append(Course(_id, _name, students))


# Enter marks
while True:
    selection = int(input(f"Select a course to enter marks (1-{numOfCourses}, 0 to quit): "))
    if selection == 0:
        break
    if selection < 1 or selection > numOfCourses:
        continue

    course = courses[selection - 1]

    for i in range(numOfStudents):
        print(f"Mark for student {students[i].getStudentName()}: ")
        mark = round(float(input()), 1)
        course.markList[i] = mark


def listCourses():
    print("Id".ljust(15), "Name")
    for c in courses:
        c.printCourse()


def listStudents():
    print("Id".ljust(15), "Name".ljust(20), "Dob")
    for s in students:
        s.printInfo()


def showMarks():
    for c in courses:
        print("\nCourse:", c.name)
        print("Id".ljust(15), "Name".ljust(20), "Mark")
        for i in range(numOfStudents):
            students[i].printNameAndId()
            print(c.markList[i])


def showAverageMarks():
    print("\nAverage mark for each student:")
    averages = []
    for i in range(numOfStudents):
        marks = [course.markList[i] for course in courses if course.markList[i] is not None]
        avg = np.average(marks) if marks else 0
        averages.append((students[i].name, avg))

    averages.sort(key=lambda x: x[1], reverse=True)

    for name, avg in averages:
        print(name.ljust(20), round(avg, 2))


# Menu
while True:
    choice = int(input(
        "\n1: List courses\n2: List students\n3: Show marks\n4: Show average marks\nOther: Quit\nChoice: "
    ))

    if choice == 1:
        listCourses()
    elif choice == 2:
        listStudents()
    elif choice == 3:
        showMarks()
    elif choice == 4:
        showAverageMarks()
    else:
        break
