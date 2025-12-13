import math
import numpy as np
import curses


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
    def __init__(self, _id, _name, _credit, studentList):
        self.id = _id
        self.name = _name
        self.credit = _credit              
        self.studentList = studentList
        self.markList = [None] * len(studentList)

    def printCourse(self):
        print(self.id.ljust(15), self.name, f"(credit: {self.credit})")

    def printMark(self, idx):
        print(self.markList[idx])


students = []
courses = []

# input number of students
numOfStudents = int(input("How many students are there in a class ? "))

# input student information
for i in range(numOfStudents):
    print(f"Student {i+1}'s informations: ")
    _id = input("Id: ")
    _name = input("Name: ")
    _dob = input("Dob (format: dd/mm/yy): ")
    students.append(Student(_id, _name, _dob))

# input number of courses
numOfCourses = int(input("How many courses are there ? "))

# input course information
for j in range(numOfCourses):
    print(f"Course {j+1}'s informations: ")
    _id = input("Id: ")
    _name = input("Name: ")
    _credit = int(input("Credit: "))        
    courses.append(Course(_id, _name, _credit, students))


# enter marks
while True:
    selection = int(input(f"Select a course to enter marks (1-{numOfCourses}, 0 to quit): "))
    if selection == 0:
        break
    if selection < 1 or selection > numOfCourses:
        continue

    course = courses[selection - 1]

    for i in range(numOfStudents):
        print(f"Mark for student {students[i].getStudentName()}: ")
        raw = float(input())

        mark = math.floor(raw * 10) / 10
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
    print("\nWeighted GPA for each student:")
    gpas = []

    for i in range(numOfStudents):
        total_weighted = 0
        total_credits = 0

        for c in courses:
            if c.markList[i] is not None:
                total_weighted += c.markList[i] * c.credit
                total_credits += c.credit

        gpa = total_weighted / total_credits if total_credits != 0 else 0
        gpas.append((students[i].name, gpa))

    # sort GPA descending
    gpas.sort(key=lambda x: x[1], reverse=True)

    for name, gpa in gpas:
        print(name.ljust(20), round(gpa, 2))


# curses 
def start_ui(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Student Mark Management System")
    stdscr.addstr(2, 0, "Use normal menu after this screen")
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(start_ui)

# Menu
while True:
    choice = int(input(
        "\n1: List courses\n2: List students\n3: Show marks\n4: Show weighted GPA\nOther: Quit\nChoice: "
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
