class Student:
    def __init__(self, _id, _name, _dob):
        self.__id = _id
        self.__name = _name
        self.__dob = _dob

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def printInfo(self):
        print(self.__id.ljust(15, " "), self.__name.ljust(20, " "), self.__dob)

    def printNameAndId(self):
        print("\t", self.__id.ljust(15, " "), self.__name.ljust(20, " "), end="")


class Course:
    def __init__(self, _id, _name, _studentList):
        self.__id = _id
        self.__name = _name
        self.studentList = _studentList
        self.markList = []   

    def getName(self):
        return self.__name

    def printCourse(self):
        print(self.__id.ljust(15, " "), self.__name)

    def printMark(self, index):
        print(self.markList[index])


class Mark:
    def __init__(self, value):
        self.__value = value

    def getValue(self):
        return self.__value





students = []
courses = []
marks = []

# Input number of students in a class
numOfStudents = int(input("How many students are there in a class ? \n"))

# Input student information
for i in range(numOfStudents):
    print(f"Student {i+1}'s information: ")
    _id = input("Id: ")
    _name = input("Name: ")
    _dob = input("Dob (format: dd/mm/yy): ")
    students.append(Student(_id, _name, _dob))

# Input number of courses
numOfCourses = int(input("How many courses are there ? \n"))

# Input course information
for j in range(numOfCourses):
    print(f"Course {j+1}'s information: ")
    _id = input("Id: ")
    _name = input("Name: ")
    courses.append(Course(_id, _name, students))

# Input marks
courseSelection = 1
while courseSelection in range(1, numOfCourses + 1):
    courseSelection = int(input(
        f"To enter marks for student, select a course (from 1 to {numOfCourses}, type 0 to quit): "
    ))

    if courseSelection == 0:
        break

    selectedCourse = courses[courseSelection - 1]
    tempMarks = []

    for k in range(numOfStudents):
        print(f"Mark for student {students[k].getName()}: ")
        value = int(input())
        tempMarks.append(value)

    selectedCourse.markList = tempMarks

# Listing functions
choices = 1

while choices < 4:
    choices = int(input(
        "If you want to see courses list, type 1; students list, type 2; student marks, type 3; others to quit: "
    ))

    # List courses
    if choices == 1:
        print("Id".ljust(15, " "), "Name")
        for c in courses:
            c.printCourse()

    # List students
    elif choices == 2:
        print("Id".ljust(15, " "), "Name".ljust(20, " "), "Dob")
        for s in students:
            s.printInfo()

    # Show student marks for all courses
    elif choices == 3:
        for c in courses:
            print(c.getName())
            print("\tId".ljust(15, " "), "Name".ljust(20, " "), "Mark")
            for i in range(numOfStudents):
                students[i].printNameAndId()
                print(c.markList[i])

    else:
        break
